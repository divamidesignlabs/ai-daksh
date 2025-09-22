#!/usr/bin/env python3
"""Build script to copy assets before packaging"""

import shutil
import sys
from pathlib import Path


def copy_assets():
    """Copy assets from root to src/daksh/ before building"""
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    assets_src = root_dir / "assets"
    assets_dest = root_dir / "src" / "daksh" / "assets"

    print("🔧 Preparing package build...")

    # Remove existing assets if they exist
    if assets_dest.exists():
        shutil.rmtree(assets_dest)
        print(f"   Removed existing assets from {assets_dest}")

    # Copy assets
    if assets_src.exists():
        shutil.copytree(assets_src, assets_dest)
        print(f"✅ Copied assets from {assets_src} to {assets_dest}")

        # List what was copied
        copied_items = list(assets_dest.iterdir())
        print(f"   Copied {len(copied_items)} items:")
        for item in sorted(copied_items):
            print(f"     - {item.name}")
    else:
        print(f"❌ Error: Assets directory not found at {assets_src}")
        sys.exit(1)


def cleanup_assets():
    """Remove copied assets after build (optional cleanup)"""
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    assets_dest = root_dir / "src" / "daksh" / "assets"

    if assets_dest.exists():
        shutil.rmtree(assets_dest)
        print(f"🧹 Cleaned up copied assets from {assets_dest}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "cleanup":
        cleanup_assets()
    else:
        copy_assets()
