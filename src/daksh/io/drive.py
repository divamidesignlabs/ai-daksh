"""Google Drive connector for listing folders and downloading files."""

from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

from torch_snippets import AD, P, makedir, write_json, Timer

from daksh.__pre_init__ import cli

class GoogleDriveClient:
    SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

    def __init__(self, credentials_path=".secrets/credentials.json", token_path=".secrets/token.json"):
        self.credentials_path = os.environ.get("GOOGLE_DRIVE_CREDENTIALS_PATH", credentials_path)
        self.token_path = os.environ.get("GOOGLE_DRIVE_TOKEN_PATH", token_path)
        self.creds = None
        self.get_credentials()
        self.service = build("drive", "v3", credentials=self.creds)

    def get_credentials(self):
        if os.path.exists(self.token_path):
            self.creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                        self.credentials_path, self.SCOPES
                )
                self.creds = flow.run_local_server(port=0)
            with open(self.token_path, "w") as token:
                token.write(self.creds.to_json())
        return self.creds
    
    def get_mime_type(self, file_id):
        """Get the MIME type of a file in Google Drive."""
        try:
            file_metadata = self.service.files().get(fileId=file_id, fields="mimeType").execute()
            return file_metadata.get("mimeType", "unknown")
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None
    
    def download_file(self, file_id, destination):
        """Download a file from Google Drive."""
        try:
            file_metadata = self.service.files().get(fileId=file_id, fields="mimeType, name").execute()
            mime_type = file_metadata["mimeType"]
            if mime_type.startswith("application/vnd.google-apps."):
                # Use export_media for Google Docs Editor files
                export_mime = {
                    "application/vnd.google-apps.document": "application/pdf",
                    "application/vnd.google-apps.spreadsheet": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    "application/vnd.google-apps.presentation": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                }.get(mime_type)

                if not export_mime:
                    print(f"Cannot export files of type {mime_type}")
                    return

                request = self.service.files().export_media(fileId=file_id, mimeType=export_mime)
            else:
                request = self.service.files().get_media(fileId=file_id)
            # request is now conditionally assigned above
            fh = open(destination, "wb")
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(f"Download {int(status.progress() * 100)}% complete.")
            fh.close()
        except HttpError as error:
            print(f"An error occurred: {error}")

    def list_drive_files_(self):
        try:
            results = (
                self.service.files()
                .list(pageSize=10, fields="nextPageToken, files(id, name, mimeType, modifiedTime, parents)")
                .execute()
            )
            items = results.get("files", [])
            if items:
                print("Files:")
                for item in items:
                    print(f"{item['name']} ({item['id']})")
            else:
                print("No files found.")
        except HttpError as error:
            print(f"An error occurred: {error}")

    def list_drive_files(self):
        from glob import glob
        import json
        files_list = sorted(glob("data/drive_files/*.json"), key=lambda x: int(P(x).stem))
        if files_list:
            last_file = files_list[-1]
            with open(last_file) as f:
                last_data = json.load(f)
            if isinstance(last_data, dict) and last_data:
                last_ix = int(P(last_file).stem)
                ix = last_ix + 1
                latest_time = min([v["modifiedTime"] for v in last_data.values()])
                q = f"modifiedTime < '{latest_time}'"
            else:
                ix = 1
                q = "modifiedTime < '2021-07-05T00:00:00'"
        else:
            ix = 1
            q = "modifiedTime < '2021-07-05T00:00:00'"
        page_token = None
        timer = Timer(1_00_000)
        while True:
            response = self.service.files().list(
                q=q,
                pageSize=100,
                fields="nextPageToken, files(id, name, mimeType, modifiedTime, parents)",
                pageToken=page_token
            ).execute()
            files = response.get('files', [])
            if not files:
                break
            to = P(f'data/drive_files/{ix}.json')
            if to.exists():
                print(f"Skipping page {ix} (already exists)")
                page_token = response.get('nextPageToken', None)
                ix += 1
                continue
            files = AD({item['id']: item for item in files})
            makedir(to.parent)
            write_json(files, to)
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                print(f"Completed listing files. Total pages: {ix}")
                break
            ix += 1
            timer()

    def upload_files(self, file_paths, mime_type=None, folder_name=None):
        """Upload multiple files to Google Drive. If folder_name is given, upload to that folder (create if needed)."""
        from googleapiclient.http import MediaFileUpload
        parent_id = None
        if folder_name:
            # Search for folder by name
            results = self.service.files().list(
                q=f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}' and trashed=false",
                spaces='drive',
                fields='files(id, name)',
                pageSize=1
            ).execute()
            folders = results.get('files', [])
            if folders:
                parent_id = folders[0]['id']
            else:
                # Create folder if not found
                folder_metadata = {
                    'name': folder_name,
                    'mimeType': 'application/vnd.google-apps.folder'
                }
                folder = self.service.files().create(body=folder_metadata, fields='id').execute()
                parent_id = folder.get('id')
        results = []
        for file_path in file_paths:
            file_metadata = {'name': os.path.basename(file_path)}
            if parent_id:
                file_metadata['parents'] = [parent_id]
            media = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)
            try:
                file = self.service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields='id, name'
                ).execute()
                print(f"Uploaded file: {file.get('name')} (ID: {file.get('id')})")
                results.append(file)
            except HttpError as error:
                print(f"An error occurred uploading {file_path}: {error}")
                results.append(None)
        return results




@cli.command(name='list-drive-files')
def list_drive_files_command():
    client = GoogleDriveClient()
    client.list_drive_files()

@cli.command(name='download-file')
def download_file_command(file_id: str, destination):
    """Download a file from Google Drive."""
    client = GoogleDriveClient()
    client.download_file(file_id, destination)

@cli.command(name='get-mime-type')
def get_mime_type_command(file_id: str):
    """Get the MIME type of a file in Google Drive."""
    client = GoogleDriveClient()
    mime_type = client.get_mime_type(file_id)
    if mime_type:
        print(f"MIME type of file {file_id}: {mime_type}")
    else:
        print(f"Could not retrieve MIME type for file {file_id}.")

@cli.command(name='search-drive-files')
def search_drive_files_command(query: str):
    """Search for files in Google Drive."""
    client = GoogleDriveClient()
    try:
        results = client.service.files().list(q=f"name contains '{query}'", pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print("No files found.")
        else:
            print("Files:")
            for item in items:
                print(f"{item['name']} ({item['id']})")
    except HttpError as error:
        print(f"An error occurred: {error}")

@cli.command(name='upload-files')
def upload_files_command(file_paths: list[str], mime_type: str = None, folder_name: str = None):
    """Upload multiple files to Google Drive. Optionally specify a folder name."""
    client = GoogleDriveClient()
    client.upload_files(file_paths, mime_type, folder_name)
"""Google Drive connector for listing folders and downloading files."""


if __name__ == "__main__":
    list_drive_files_command()
