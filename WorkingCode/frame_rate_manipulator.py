import ffmpeg

input_file = ffmpeg.input('output_video.mp4')

reduced_fps_output_file = ffmpeg.output(
    input_file,
    'reduced_fps_output.mp4',
    r=1  # set output frame rate to 30 fps
)

reduced_fps_output_file = reduced_fps_output_file.global_args('-loglevel', 'error')  # suppress output logs

ffmpeg.run(reduced_fps_output_file)