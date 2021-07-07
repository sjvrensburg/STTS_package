import subprocess

from itertools import tee
from typing import Iterator, Tuple, List


def pairwise(iterable: list) -> Iterator[Tuple[float, float]]:
    """ 
    Takes an iterable, `s`, and creates iterator of the form 
        s -> (s0,s1), (s1,s2), (s2, s3), ...
    
    Recipe taken from:
        https://docs.python.org/3.7/library/itertools.html
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def get_video_duration(filename: str) -> float:
    """
    Determine the duration of the video.

    NOTE: Code is based on:
        https://github.com/DarkTrick/python-video-silence-cutter/blob/master/silence_cutter.py
    """
    command = ["ffprobe","-i",filename,"-v","quiet",
                "-show_entries","format=duration","-hide_banner",
                "-of","default=noprint_wrappers=1:nokey=1"]

    output = subprocess.run(command, stdout=subprocess.PIPE)
    s = str(output.stdout, "UTF-8")
    return float(s)


def find_silences(
    filename: str, duration: float = 1, dB: float = -35) -> Tuple[List, bool]:
    """
    Find stretches of silence.

    This function uses ffmpeg to find stretches of silence.

    ARGUMENTS:
    filename (str):     The file (and path) to search.
    duration (float):   Minimum duration of silence to record.
    dB (float):         Volume threshold. Anything below it is considered silence.

    RETURNS:
    Returns a tuple. The first element of the tuple is a list of start/end times.
    The second element of the tuple indicates whether the video starts with silence.

    NOTE: Code is based on:
        https://github.com/DarkTrick/python-video-silence-cutter/blob/master/silence_cutter.py
    """
    # Find sections of silence using ffmpeg
    command = ["ffmpeg","-i",filename,
                "-af","silencedetect=n=" + str(dB) + "dB:d=" + str(duration),
                "-f","null","-"]
    output = subprocess.run (command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s = str(output)
    lines = s.split("\\n")

    # Extract the start and end times of sections of silence.
    time_list = []
    for line in lines:
        if "silencedetect" in line:
            words = line.split(" ")
            for i in range(len(words)):
                if "silence_start" in words[i]:
                    time_list.append(float(words[i+1]))
                if "silence_end" in words[i]:
                    time_list.append(float (words[i+1]))
    
    # Check there were periods of silence.
    if len(time_list) < 1:
        raise Exception("Did not find any sections of silence.")

    # Check whether silence starts at 0.
    silent_start = False
    if time_list[0] == 0:
        silent_start = True
    if not silent_start:
        time_list.insert(0, 0)

    # If necessary, append the final time equals the duration of the video.
    dur = get_video_duration(filename)
    if time_list[len(time_list)-1] != dur:
        time_list.append(dur)
    
    return time_list, silent_start