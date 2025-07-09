
# Audio & Video Transcriber Using Python

This project provides a simple Python script to automatically transcribe audio and video files to text using OpenAI's Whisper model. It recursively scans a specified input directory for supported media files, transcribes their content, and saves the results as text files in an output directory.

---

## Features

- **Automatic Transcription:** Converts speech in audio and video files to text using Whisper.
- **Batch Processing:** Recursively scans folders and processes all supported files.
- **Multiple Formats Supported:** Works with `.mp3`, `.wav`, `.mp4`, `.m4a`, `.flac`, `.aac`, `.ogg`, `.wma`, `.mov`, `.avi`, `.mkv` and more.
- **Easy Output:** Saves each transcript as a `.txt` file named after the original media file.

---

## Requirements

- Python 3.11 or newer
- [openai-whisper](https://github.com/openai/whisper) (`pip install openai-whisper`)
- [ffmpeg](https://ffmpeg.org/) (required for many audio/video formats)

---

## Usage

1. **Set Input and Output Directories:**
   - Edit the `input_directory` and `output_directory` variables in `audio_video_Transcriber.py` to point to your folders.

2. **Install Dependencies:**
   ```bash
   pip install openai-whisper
   # On Ubuntu/Debian:
   sudo apt-get install ffmpeg
   # Or use your OS package manager for ffmpeg
   ```

3. **Run the Script:**
   ```bash
   python audio_video_Transcriber.py
   ```

4. **Check Output:**
   - Transcripts will be saved as `.txt` files in your output directory, named after each media file.

---

## Example

Sample input and output files are provided in the `sample_input and output/` folder.

---

## Notes

- The script uses the smallest Whisper model (`tiny`) for speed. For better accuracy, you can change the model in the script.
- Make sure you have permission to read from the input directory and write to the output directory.
- For large files or better accuracy, consider using a larger Whisper model (see [Whisper documentation](https://github.com/openai/whisper)).
