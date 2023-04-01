import ffmpeg
import os


def folder_content_audio_converter(input_folder, out_folder):
    for file_name in os.scandir(input_folder):
        in_file = ffmpeg.input(file_name.path)
        out_WAV = os.path.join(out_folder, "WAV" + file_name.name[:-4] + ".wav")
        ffmpeg.output(in_file, out_WAV, format='wav', acodec='pcm_s16le').run()

def directory_organizer(split_file_dir, destination_directory):
    for folder_name in os.listdir(split_file_dir):
        if folder_name.endswith("_audio"): 
            input_folder = os.path.join(split_file_dir, folder_name)
            wav_directory = os.path.join(destination_directory, os.path.splitext(folder_name)[0] + "wav_audio") 
            os.makedirs(wav_directory, exist_ok=True)
            folder_content_audio_converter(input_folder=input_folder, out_folder=wav_directory)

# User Input
directory_organizer(split_file_dir="drafts/earlier_versions/Blackcanary-Split", destination_directory="drafts/experimental_wav_dir")
