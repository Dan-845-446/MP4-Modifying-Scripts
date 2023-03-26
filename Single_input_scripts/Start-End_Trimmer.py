import os
import ffmpeg


def trim_video(in_file, out_file, start_trim, end_trim):
    # Delete output file if it already exists
    if os.path.exists(out_file):
        os.remove(out_file)

    # Probe input file to get its duration
    in_file_probe_result = ffmpeg.probe(in_file)
    in_file_duration = float(in_file_probe_result.get("format", {}).get("duration", None))

    # Calculate new start and end points
    new_start = start_trim
    new_end = min(in_file_duration, in_file_duration - end_trim)

    # Create FFMPEG input stream
    input_stream = ffmpeg.input(in_file)

    pts = "PTS-STARTPTS"
    # Trim video and audio streams
    video = input_stream.video.trim(start=new_start, end=new_end).setpts(pts)
    audio = input_stream.audio.filter("atrim", start=new_start, end=new_end).filter_("asetpts", pts)

    # Set output format and codec
    output = ffmpeg.output(video, audio, out_file, format="mp4")

    # Run FFMPEG command to trim the video
    ffmpeg.run(output)


trim_video(".venv\movie.mp4", "newtrim4.mp4", start_trim=5, end_trim=5)