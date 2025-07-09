----------------------------------------
#Script Name: Audio Transcription Script
----------------------------------------

Purpose:
----------------------------------------
This script recursively scans a specified directory for supported media files (such as MP3, WAV, MP4, etc.), transcribes the audio content to text using OpenAI's Whisper model, and saves the transcription as text files in the output directory.


Model Setup:
----------------------------------------
The script loads the smallest available Whisper model (tiny).

Supported Media Types:
----------------------------------------
The script supports the following media file extensions:

.mp3, .wav, .mp4, .m4a, .flac, .aac, .ogg, .wma, .mov, .avi, .mkv.
Directory Traversal:
It scans the given input directory recursively and processes all media files it finds.

Transcription:
----------------------------------------
For each media file, it uses the Whisper model to transcribe the audio to text.

Output:
----------------------------------------
The transcribed text is saved as .txt files in the specified output directory. Each file is named based on the corresponding media file (with .txt extension).

How to Use:
----------------------------------------
-Set the Input Directory:
Update the input_directory variable to point to the folder containing your media files.

-Set the Output Directory:
Update the output_directory variable to point to the folder where you want the transcriptions to be saved.

-Run the Script:
Execute the script. It will process all supported media files in the input directory, transcribe the audio, and save the results in the output folder.

Requirements:
----------------------------------------
Python 3.11
Whisper model installed (pip install openai-whisper)
ffmpeg (for handling certain audio and video formats)

Notes:
----------------------------------------
The script uses the smallest Whisper model (tiny) for faster transcription, but larger models may provide better accuracy.
The script assumes that you have the necessary permissions to read files from the input directory and write to the output directory.
