import ffmpeg

input_path = 'output_audio.mp3'

(
    ffmpeg
    .input(input_path)
    .output('output_wav.wav', format='wav')
    .run()
)
