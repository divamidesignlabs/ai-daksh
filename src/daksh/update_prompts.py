import shutil
from torch_snippets import *

from .__pre_init__ import cli


@cli.command()
def update_prompts(dry_run: bool = False):
    prompts_folder: P = current_file_dir(__file__) / "prompt-templates"
    for f in ls(prompts_folder):
        to = f"./{f.name}"
        Info(f"Updating {f} to {to}")

        if dry_run:
            continue

        if f.is_file():
            f.cp(to)
        elif f.is_dir():
            shutil.copytree(f, to, dirs_exist_ok=True)
