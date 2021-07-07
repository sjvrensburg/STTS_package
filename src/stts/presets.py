
# Presets:
# Export at highest quality for additional
# processing
# TODO: This is actually terrible
lossless = {
    "codec": "mpeg4", # "png",
    "preset": "ultrafast",
    "threads": 4}

# Encode using the settings that I use for
# slide decks in shotcut.
slides = {
    "fps": 30,
    "codec": "libx264",
    "bitrate": None,
    "audio": True,
    "audio_fps": 44100,
    "preset": 'slow',
    "audio_nbytes": 4,
    "audio_codec": "aac",
    "audio_bitrate": '80k',
    "audio_bufsize": 2000,
    "temp_audiofile": None,
    "rewrite_audio": True,
    "remove_temp": True,
    "write_logfile": False,
    "verbose": True,
    "threads": 4,
    "ffmpeg_params": ['-crf', '27', '-movflags', '+faststart'],
    "logger": 'bar'}