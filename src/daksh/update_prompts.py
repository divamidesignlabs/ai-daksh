import hashlib, shutil
from torch_snippets import Info, current_file_dir, ls, P

from .__pre_init__ import cli


def get_md5_hash(file_path: P) -> str:
    """Calculate MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        Info(f"Error calculating hash for {file_path}: {e}")
        return ""


def copy_file_with_comparison(source: P, destination: P, dry_run: bool = False) -> bool:
    """
    Copy a file from source to destination and compare MD5 hashes.
    Returns True if file was updated (different hashes or new file).
    """
    destination_path = P(destination)
    
    # Calculate source hash
    source_hash = get_md5_hash(source)
    if not source_hash:
        Info(f"❌ Failed to calculate hash for source: {source}")
        return False
    
    # Check if destination exists and calculate its hash
    destination_exists = destination_path.exists()
    destination_hash = ""
    
    if destination_exists:
        destination_hash = get_md5_hash(destination_path)
        if not destination_hash:
            Info(f"❌ Failed to calculate hash for destination: {destination_path}")
            return False
    
    # Compare hashes
    file_updated = not destination_exists or source_hash != destination_hash
    
    if file_updated:
        status = "🆕 NEW" if not destination_exists else "🔄 UPDATED"
        Info(f"**** {status}: {source} -> {destination}")
        if destination_exists:
            Info(f"     Source hash:      {source_hash}")
            Info(f"     Destination hash: {destination_hash}")
        else:
            Info(f"     Hash: {source_hash}")
        
        if not dry_run:
            try:
                # Ensure parent directory exists
                destination_path.parent.mkdir(parents=True, exist_ok=True)
                source.cp(destination)
                Info(f"✅ Successfully copied: {destination}")
            except Exception as e:
                Info(f"❌ Error copying file: {e}")
                return False
    else:
        Info(f"⏭️  UNCHANGED: {source} (hashes match)")
    
    return file_updated


def copy_directory_recursive(source_dir: P, destination_base: str, dry_run: bool = False) -> dict:
    """
    Recursively copy all files and directories from source to destination.
    Returns a summary of the operation.
    """
    summary = {
        "total_files": 0,
        "updated_files": 0,
        "new_files": 0,
        "unchanged_files": 0,
        "errors": 0
    }
    
    def _recursive_copy(current_source: P, current_dest_path: str, depth: int = 0):
        indent = "  " * depth
        Info(f"{indent}📁 Processing directory: {current_source}")
        
        for item in ls(current_source):
            if item.is_file():
                # Calculate relative path for destination
                relative_path = item.relative_to(source_dir)
                destination_file = P(destination_base) / relative_path
                
                summary["total_files"] += 1
                
                Info(f"{indent}📄 Processing file: {item}")
                
                try:
                    was_updated = copy_file_with_comparison(item, destination_file, dry_run)
                    
                    if was_updated:
                        if destination_file.exists() and not dry_run:
                            summary["updated_files"] += 1
                        else:
                            summary["new_files"] += 1
                    else:
                        summary["unchanged_files"] += 1
                        
                except Exception as e:
                    Info(f"{indent}❌ Error processing {item}: {e}")
                    summary["errors"] += 1
                    
            elif item.is_dir():
                Info(f"{indent}📁 Entering subdirectory: {item}")
                _recursive_copy(item, current_dest_path, depth + 1)
    
    _recursive_copy(source_dir, destination_base)
    return summary


@cli.command()
def update_prompts(dry_run: bool = False):
    """
    Update prompt templates by copying them recursively from source to destination.
    Compares MD5 hashes to determine which files need updating.
    """
    prompts_folder: P = current_file_dir(__file__) / "prompt-templates"
    destination_base = "./"

    shutil.rmtree("./.github/prompts", ignore_errors=True)
    shutil.rmtree("./.copilot-instructions.md", ignore_errors=True)
    
    Info(f"🚀 Starting recursive update from {prompts_folder} to {destination_base}")
    Info(f"💡 Dry run mode: {'ON' if dry_run else 'OFF'}")
    Info("=" * 80)
    
    if not prompts_folder.exists():
        Info(f"❌ Source directory does not exist: {prompts_folder}")
        return
    
    try:
        summary = copy_directory_recursive(prompts_folder, destination_base, dry_run)
        
        Info("=" * 80)
        Info("📊 OPERATION SUMMARY:")
        Info(f"   📁 Total files processed: {summary['total_files']}")
        Info(f"   🔄 Files updated: {summary['updated_files']}")
        Info(f"   🆕 New files created: {summary['new_files']}")
        Info(f"   ⏭️  Files unchanged: {summary['unchanged_files']}")
        Info(f"   ❌ Errors encountered: {summary['errors']}")
        
        if dry_run:
            Info("💡 This was a dry run - no files were actually modified")
            
    except Exception as e:
        Info(f"❌ Fatal error during operation: {e}")
        raise
