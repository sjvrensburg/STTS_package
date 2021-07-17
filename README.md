# STTSilence

STTSilence, short for "Speed through the silence", is utility that speeds up the silent parts in a video. This is especially useful for lectures and slidecasts.

## Installation

This module depends on MoviePy. However, due to some issues with the current stable release of MoviePy, STTSilence uses the development version of MoviePy. At the time of writing, this is version 2.0.0.dev2.

**NOTE:** Given the changes version 2 of MoviePy, the current stable release of MoviePy is incompatible with STTSilence. Therefore, you _must_ install MoviePy from Github. Use the following command:
```
pip install git+https://github.com/Zulko/moviepy.git
```

Once you have installed MoviePy, one may install STTSilence from Github. Use the following command:
```
https://github.com/sjvrensburg/STTS_package.git
```

STTSilence does not require any additional dependencies beyond that required by MoviePy.

## Usage

The main function provided by this module is `stts`. This function is responsible for speeding up the silent parts of a video.

```python
from stts import stts

in_file = "video_with_annoying_pauses.mp4"
out_file = "video_with_fewer_annoying_pauses.mp4"

duration  = 0.5  # Minimum duration of silence to speed up.
threshold = -35  # This will classify anything below 35dB as "silence".
speed     = 3    # Make silent sections 3 times faster.

# This will produce the file `out_file`.
stts(in_file, out_file, duration, threshold, speed)
```

It is also useful to create a script that you can run from the command line.
