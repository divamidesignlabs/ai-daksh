#!/usr/bin/env python3
# filepath: scripts/convert_all_to_markdown.py

import os
import subprocess
import time
from pathlib import Path
import torch
import soundfile as sf
import librosa
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Initialize Whisper model globally (only when needed)
whisper_model = None
whisper_processor = None
device = None

def initialize_whisper():
    """Initialize the Whisper model for audio transcription"""
    global whisper_model, whisper_processor, device
    
    if whisper_model is None:
        print("Initializing Whisper model (this may take a moment)...")
        whisper_processor = WhisperProcessor.from_pretrained("openai/whisper-large-v3")
        whisper_model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v3")
        
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {device}")
        whisper_model.to(device)
        whisper_model.eval()
        print("Whisper model initialized successfully")

def is_audio_file(file_path):
    """Check if the file is an audio file based on extension"""
    audio_extensions = ['.mp3', '.wav', '.m4a', '.ogg', '.flac', '.aac', '.wma', '.webm']
    return file_path.suffix.lower() in audio_extensions

def transcribe_audio(audio_path, output_path):
    """Transcribe audio file using Whisper model"""
    try:
        # Initialize Whisper if not already loaded
        initialize_whisper()
        
        # Create a temporary WAV file if not already a WAV
        wav_path = audio_path
        if audio_path.suffix.lower() != '.wav':
            wav_path = audio_path.parent / f"{audio_path.stem}_temp.wav"
            
            # Convert to WAV using ffmpeg
            subprocess.run(
                [
                    "ffmpeg",
                    "-y",
                    "-i",
                    str(audio_path),
                    "-ar",
                    "16000",
                    "-ac",
                    "1",
                    "-f",
                    "wav",
                    str(wav_path),
                ],
                check=True,
                capture_output=True,
            )
        
        # Load and preprocess audio
        input_audio, sr = sf.read(str(wav_path))
        if sr != 16000:
            input_audio = librosa.resample(input_audio, orig_sr=sr, target_sr=16000)
            sr = 16000
            
        # Chunk audio into 30-second segments for Whisper
        chunk_size = 16000 * 30  # 30 seconds at 16kHz
        num_chunks = int(len(input_audio) / chunk_size) + (
            1 if len(input_audio) % chunk_size != 0 else 0
        )
        
        print(f"Transcribing {num_chunks} chunks from audio file...")
        transcripts = []
        for i in range(num_chunks):
            print(f"Processing chunk {i+1}/{num_chunks}...")
            chunk = input_audio[i * chunk_size : (i + 1) * chunk_size]
            inputs = whisper_processor(chunk, sampling_rate=16000, return_tensors="pt").to(device)
            with torch.no_grad():
                predicted_ids = whisper_model.generate(inputs["input_features"])
                transcription = whisper_processor.batch_decode(
                    predicted_ids, skip_special_tokens=True
                )[0]
            transcripts.append(transcription)
        
        # Combine all transcriptions
        full_transcript = " ".join(transcripts)
        
        # Create a markdown file with the transcript
        markdown_content = f"""# Audio Transcript: {audio_path.stem}

## Overview
- **File:** {audio_path.name}
- **Duration:** {len(input_audio)/sr:.2f} seconds
- **Transcription Date:** {time.strftime("%Y-%m-%d")}

## Transcript

{full_transcript}
"""
        
        # Write to output file
        output_path.write_text(markdown_content, encoding='utf-8')
        
        # Clean up temporary file if created
        if wav_path != audio_path and wav_path.exists():
            wav_path.unlink()
            
        return True
    
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return False

def convert_to_markdown(input_path, output_folder=None):
    """Convert a file to markdown using appropriate method based on file type"""
    
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
    
    # Check if it's an audio file
    if is_audio_file(input_path):
        print(f"Detected audio file: {input_path}")
        return transcribe_audio(input_path, output_path)
    else:
        # Use markitdown (ts mkd) for non-audio files
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
    parser.add_argument("--skip-audio", action="store_true", help="Skip audio file transcription")
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