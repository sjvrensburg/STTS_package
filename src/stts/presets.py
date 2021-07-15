
# Presets:
# Settings suitable for a slide deck. Based on that
# in shotcut.
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
    "remove_temp": True,
    "write_logfile": False,
    "threads": 4,
    "ffmpeg_params": ['-crf', '27', '-movflags', '+faststart'],
    "logger": 'bar'}