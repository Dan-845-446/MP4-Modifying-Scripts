import ffmpeg
import os


def folder_frame_rate_modifier(in_folder, out_folder, fps:int):
     for file_name in os.scandir(in_folder):
         in_file = ffmpeg.input(file_name.path)
         altered_video = os.path.join(out_folder, "altered_FR" + file_name.name)
         ffmpeg.output(in_file, altered_video, r=1).run()
  

#User Input
folder_frame_rate_modifier(in_folder='drafts\\out_video', 
out_folder='drafts\\reducedFRvideos',
fps=10)