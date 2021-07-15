from stts.presets import slides

from tqdm import tqdm
from moviepy.editor import VideoFileClip, vfx, concatenate_videoclips
from stts.helper_functions import pairwise, find_silences


def stts(infile: str, outfile: str, duration: float=0.5, threshold: float=35, speed: float=3, preset: dict=slides):
    """
    stts(input: str, output: str, duration: float, threshold: float, speed: float, preset: dict)

    Function takes a video file, identifies silent sections, speeds up those sections
    and then writes the results to a new video file.

    Arguments:
    infile:     The name/path of the video file to process.
    outfile:    The name/path of the video file to output.
    duration:   The minimum duration (in seconds) of silence to detect. Sections of
                silence below this value will be ignored. Default is 0.5.
    threshold:  The loudness threshold. Anything softer than this threshold is
                considered "silence". The default value is 35 dB.
    speed:      The factor by which to speed up silent sections. Default value is 3.
    preset:     A dictionary of arguments to pass to moviepy's `write_videofile` method.
                Default value is the `slides` preset in `presets.py`.
    """
    # Identify the clip times.
    times, silent = find_silences(infile, duration, threshold)
    # Import the video
    video = VideoFileClip(infile)
    # Create the clips
    clips = []
    print("Identifying the silent sections...")
    for clip_start, clip_end in tqdm(pairwise(times)):
        # If silent, speed up by speedsilent else speednonsilent.
        speed_ = 1
        if silent:
            speed_ = speed
        # Create and append clip.
        clips.append(
            (video.subclip(clip_start, clip_end)
            .multiply_volume(int(not silent))
            .fx(vfx.multiply_speed, speed_)))
        silent = not silent
    
    final_video = concatenate_videoclips(clips)
    final_video.write_videofile(outfile, **preset)
