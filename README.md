# STTSilence

STTSilence, short for "Speed through the silence", is utility that speeds up the silent parts in a video. This is especially useful for lectures and slidecasts. 

## Installation

????

## Usage

The main function provided by this module is `stts`. This function is responsible for speeding up the silent parts of a video.

```python
# FIXME: At the moment, this doesn't work.
#   from stts import stts
# Rather, you have to go...
from stts.stts import stts

in_file = "video_with_annoying_pauses.mp4"
out_file = "video_with_fewer_annoying_pauses.mp4"

duration = 0.5  # Minimum duration of silence to speed up.
threshold = 35  # This will classify anything below 35dB as "silence".
speed = 3       # Make silent sections 3 times faster.

# This will produce the file `out_file`.
stts(in_file, out_file, duration, threshold, speed)
```

It is also useful to create a script that you can run from the command line.