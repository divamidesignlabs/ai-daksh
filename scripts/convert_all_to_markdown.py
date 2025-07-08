#!/usr/bin/env python3
# filepath: scripts/convert_all_to_markdown.py

import os
import subprocess
import time
from pathlib import Path

def convert_to_markdown(input_path, output_folder=None):
    """Convert a file to markdown using ts mkd command"""
    
    input_path = Path(input_path)
    
    if not input_path.exists():
        print(f"File not found: {input_path}")
        return False
        
    # Create output path - either in same folder or specified output folder
    if output_folder:
        output_path = Path(output_folder) / f"{input_path.stem}.md"
        os.makedirs(output_folder, exist_ok=True)
    else:
        output_path = input_path.parent / f"{input_path.stem}.md"
    
    # Skip if output already exists to avoid errors
    if output_path.exists():
        print(f"Output already exists, skipping: {output_path}")
        return True
        
    # Build and run the ts mkd command
    try:
        cmd = ["ts", "mkd", str(input_path), "--output", str(output_path)]
        print(f"Running: {' '.join(cmd)}")
        
        # Run the command
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Successfully converted: {input_path} → {output_path}")
            return True
        else:
            print(f"Error converting {input_path}: {result.stderr}")
            return False
    except Exception as e:
        print(f"Exception while converting {input_path}: {e}")
        return False

def process_directory(root_path, output_root=None):
    """Process all files in a directory and its subdirectories"""
    
    root_path = Path(root_path)
    converted_count = 0
    error_count = 0
    
    # Create parallel output structure if specified
    if output_root:
        output_root = Path(output_root)
        os.makedirs(output_root, exist_ok=True)
    
    # Get all files in the directory and subdirectories
    for dirpath, dirnames, filenames in os.walk(root_path):
        current_dir = Path(dirpath)
        
        # Create corresponding output directory if needed
        if output_root:
            rel_path = current_dir.relative_to(root_path)
            current_output_dir = output_root / rel_path
            os.makedirs(current_output_dir, exist_ok=True)
        else:
            current_output_dir = None
            
        print(f"\nProcessing directory: {current_dir}")
        
        # Process each file
        for filename in filenames:
            file_path = current_dir / filename
            
            # Skip if already a markdown file
            if file_path.suffix.lower() == ".md":
                print(f"Skipping existing markdown file: {file_path}")
                continue
                
            # Skip hidden files
            if filename.startswith("."):
                continue
                
            print(f"Converting: {file_path}")
            success = convert_to_markdown(file_path, current_output_dir)
            
            if success:
                converted_count += 1
            else:
                error_count += 1
                
            # Small delay to avoid overwhelming the system
            time.sleep(0.5)
    
    return converted_count, error_count

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Convert all files in a directory to Markdown")
    parser.add_argument("input_dir", help="Directory containing files to convert")
    parser.add_argument("--output", help="Output directory for markdown files (optional)")
    args = parser.parse_args()
    
    print(f"Starting conversion of all files in: {args.input_dir}")
    if args.output:
        print(f"Output directory: {args.output}")
    
    converted, errors = process_directory(args.input_dir, args.output)
    
    print(f"\nConversion complete:")
    print(f"- Successfully converted: {converted} files")
    print(f"- Errors: {errors} files")
    
    if errors > 0:
        print("\nSome files could not be converted. Check the log above for details.")
    else:
        print("\nAll files converted successfully!")