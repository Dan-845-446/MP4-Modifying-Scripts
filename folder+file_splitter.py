import ffmpeg
import os

input_dir = ".venv\\output_folder"
output_audio_dir = ".venv\\drafts\\out_audio"
output_video_dir = ".venv\\drafts\\out_video"

for file_name in os.scandir(input_dir):
    input_file = ffmpeg.input(file_name.path)
    output_audio_file = os.path.join(output_audio_dir, "audio_only" + file_name.name)
    output_video_file = os.path.join(output_video_dir, "video_only" + file_name.name)

    output_video_file_path = os.path.join(output_video_dir, "video.mp4" + file_name.name)
    output_audio_file_path = os.path.join(output_audio_dir, "audio.mp3" + file_name.name)

    output_video = ffmpeg.output(input_file['v'], output_video_file_path)
    output_audio = ffmpeg.output(input_file['a'], output_audio_file_path)

    ffmpeg.run(output_video)
    ffmpeg.run(output_audio)
