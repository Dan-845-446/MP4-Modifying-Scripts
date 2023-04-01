import os
import ffmpeg


def trim_short_video(in_file, out_file, start_trim, end_trim):
    
    in_file_probe_result = ffmpeg.probe(in_file)
    in_file_duration = float(in_file_probe_result.get("format", {}).get("duration", None))

    new_start = start_trim
    new_end = min(in_file_duration, in_file_duration - end_trim)

    input_stream = ffmpeg.input(in_file)

    pts = "PTS-STARTPTS"
    video = input_stream.video.trim(start=new_start, end=new_end).setpts(pts)
    audio = input_stream.audio.filter("atrim", start=new_start, end=new_end).filter_("asetpts", pts)

    output = ffmpeg.output(video, audio, out_file, format="mp4")

    ffmpeg.run(output)

def trim_long_video(in_file, out_file, start_trim, end_trim):
    
    in_file_probe_result = ffmpeg.probe(in_file)
    in_file_duration = float(in_file_probe_result.get("format", {}).get("duration", None))

    new_start = start_trim
    new_end = min(in_file_duration, in_file_duration - end_trim)

    input_stream = ffmpeg.input(in_file)

    pts = "PTS-STARTPTS"
    video = input_stream.video.trim(start=new_start, end=new_end).setpts(pts)
    audio = input_stream.audio.filter("atrim", start=new_start, end=new_end).filter_("asetpts", pts)

    output = ffmpeg.output(video, audio, out_file, format="mp4")

    ffmpeg.run(output)

def trim_folder(in_folder, out_folder):
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
       
    for file_name in os.listdir(in_folder):
        if file_name.endswith(".mp4"):
            in_file = os.path.join(in_folder, file_name)
            out_file = os.path.join(out_folder,  "_trimmed_"+file_name)
           
            in_file_probe_result = ffmpeg.probe(in_file)
            in_file_duration = float(in_file_probe_result.get("format", {}).get("duration", None))

            if in_file_duration <= 10:
                trim_short_video(in_file, out_file, start_trim=1, end_trim=1)
            elif in_file_duration > 10:
                trim_long_video(in_file, out_file, start_trim=2, end_trim=2)    
            
            print(f"_trimmed {in_folder}+{file_name} to {out_file}")
        else:
            print("error on file"+file_name)

def folder_organizer(Mother_folder, out_cluster):
    for folder_name in os.listdir(Mother_folder): 
        in_folder = os.path.join(Mother_folder, folder_name)
        out_folder = os.path.join(out_cluster, folder_name + "_trimmed_")
        trim_folder(in_folder, out_folder)


#User Input:
folder_organizer("Blackcanary-Reviewed_Downloads","Blackcanary-Trimmed")