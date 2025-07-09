import os
import whisper

import warnings
warnings.filterwarnings("ignore")

# Set up the Whisper model (smallest available model)
model = whisper.load_model("tiny")

# Supported media file extensions
MEDIA_EXTENSIONS = {".mp3", ".wav", ".mp4", ".m4a", ".flac", ".aac", ".ogg", ".wma", ".mov", ".avi", ".mkv"}


def transcribe_file(file_path):
    """Transcribes an audio/video file using Whisper."""
    print(f"Transcribing: {file_path}")
    result = model.transcribe(file_path)
    return result["text"]


def process_directory(input_folder, output_folder):
    """Recursively scans the input directory for media files and transcribes them."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(input_folder):
        for file in files:
            if any(file.lower().endswith(ext) for ext in MEDIA_EXTENSIONS):
                file_path = os.path.join(root, file)
                output_file = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.txt")

                # Transcribe and save the result
                transcript = transcribe_file(file_path)
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(transcript)

                print(f"Saved transcript: {output_file}")


if __name__ == "__main__":
    input_directory = r"C:\Aditya\IdealabsProject\input_files"
    output_directory = (r"C:\Aditya\IdealabsProject\output_files")

    process_directory(input_directory, output_directory)
