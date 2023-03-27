import ffmpeg
import os

def folder_content_audio_converter(input_folder, out_folder):
    for file_name in os.scandir(input_folder):
        in_file = ffmpeg.input(file_name.path)
        out_WAV = os.path.join(out_folder, "WAV" + file_name.name)
        ffmpeg.output(in_file, out_WAV, format='wav').run()
       
#User Input
folder_content_audio_converter(".venv\\drafts\\out_audio", ".venv\\drafts\\WAVs")
