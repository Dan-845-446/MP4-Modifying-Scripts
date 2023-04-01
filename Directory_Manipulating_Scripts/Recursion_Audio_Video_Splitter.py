import os
import ffmpeg
 

def folder_organizer(Mother_folder, out_directory):
    for folder_name in os.scandir(Mother_folder): 
        in_folder = os.path.realpath(folder_name, strict=False)
    
        audio_dir_path = os.path.join(out_directory, folder_name.name + "_isolated_audio") 
        os.makedirs(audio_dir_path, exist_ok=True)
    
        video_dir_path = os.path.join(out_directory, folder_name.name + "_isolated_video")
        os.makedirs(video_dir_path, exist_ok=True)         
    
        for file_name in os.scandir(in_folder):
            input_file = ffmpeg.input(file_name.path)
                
            output_video_folder = os.path.join(video_dir_path, "video_only" + file_name.name)
            output_audio_folder = os.path.join(audio_dir_path, "audio_only" + file_name.name)

            output_video = ffmpeg.output(input_file['v'], output_video_folder)
            output_audio = ffmpeg.output(input_file['a'], output_audio_folder)

            ffmpeg.run(output_video)
            ffmpeg.run(output_audio)
                

#User Input:
folder_organizer("Blackcanary-Trimmed", "drafts/earlier_versions/Blackcanary-Split")