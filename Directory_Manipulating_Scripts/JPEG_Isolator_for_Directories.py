import os
import ffmpeg

def directory_organizer(Input_Directory, JPEG_Directory):
    for folder_name in os.scandir(Input_Directory):
        in_folder = os.path.realpath(folder_name, strict=False)

        jpeg_folder = os.path.join(JPEG_Directory, folder_name.name + "_JPEGs")
        os.makedirs(jpeg_folder, exist_ok=True)
        core_function(in_folder, jpeg_folder)

def core_function(in_folder, jpeg_folder):
        for file_name in os.scandir(in_folder):
            input_video = ffmpeg.input(file_name.path)
            output_file = ffmpeg.output(input_video, os.path.join(jpeg_folder, f"{file_name.name}_%d.jpg"), vf='fps=1/3')
            ffmpeg.run(output_file)

            jpeg_files = sorted([f for f in os.listdir(jpeg_folder) if f.startswith(file_name.name)])
            if len(jpeg_files) > 4:
                for extra_file in jpeg_files[4:]:
                    os.remove(os.path.join(jpeg_folder, extra_file))

#User Input:
directory_organizer(Input_Directory="Reduced Frame Rate Sample Directory", JPEG_Directory="JPEG Folders")