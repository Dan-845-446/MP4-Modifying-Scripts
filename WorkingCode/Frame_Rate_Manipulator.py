import ffmpeg
import os


def folder_frame_rate_modifier(in_folder, out_folder, r):
     for file_name in os.scandir(in_folder):
         in_file = ffmpeg.input(file_name.path)
         altered_video = os.path.join(out_folder, "altered_FR" + file_name.name)
         ffmpeg.output(in_file, altered_video, r=r).run()
  

def directory_organizer(split_file_dir, destination_directory, fps):
    for folder_name in os.listdir(split_file_dir):
        if folder_name.endswith("_video"): 
            input_folder = os.path.join(split_file_dir, folder_name)
            modified_fps_directory = os.path.join(destination_directory, os.path.splitext(folder_name)[0] + "modified_fps") 
            os.makedirs(modified_fps_directory, exist_ok=True)
            folder_frame_rate_modifier(in_folder=input_folder, out_folder=modified_fps_directory, r=fps)


#User Input
directory_organizer(split_file_dir="drafts\earlier_versions\Blackcanary-Split",
                     destination_directory="drafts\earlier_versions\experimental_mfps_dir",
                       fps=1)