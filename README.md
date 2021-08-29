**NOTE: There are far better tools available for the task of speeding up silent sections. I highly recommend that you rather use [unsilence](https://github.com/lagmoellertim/unsilence) or my simple front-end to it, which is part of the [PPVID](https://github.com/sjvrensburg/ppvid) set of tools.**

# STTSilence

STTSilence, short for "Speed through the silence", is utility that speeds up the silent parts in a video. This is especially useful for lectures and slidecasts.

## Installation

This module depends on [MoviePy](https://github.com/Zulko/moviepy). However, due to some issues with the current stable release of [MoviePy](https://github.com/Zulko/moviepy), STTSilence uses the development version of [MoviePy](https://github.com/Zulko/moviepy). At the time of writing, this is version 2.0.0.dev2.

**NOTE:** Given the changes in version 2 of [MoviePy](https://github.com/Zulko/moviepy), the current stable release of [MoviePy](https://github.com/Zulko/moviepy) is incompatible with STTSilence. Therefore, you _must_ install [MoviePy](https://github.com/Zulko/moviepy) from Github. Use the following command:
```
pip install git+https://github.com/Zulko/moviepy.git
```

Once you have installed [MoviePy](https://github.com/Zulko/moviepy), one may install STTSilence from Github. Use the following command:
```
pip install git+ https://github.com/sjvrensburg/STTS_package.git
```

STTSilence does not require any additional dependencies beyond that required by [MoviePy](https://github.com/Zulko/moviepy).

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
