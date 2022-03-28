# TheArtOfSubtitles
Tools of a movie-freak.
## SubtitleGenerator
Ever downloaded a "not so popular" movie, for which no subtitle exists on the internet?

The file SubGen.py can generate live subtitles along the video file if the sound queality is somehow clear. It shows the subtitles in a transparent topmost window, so unless the video file is played fullscreen, it should be visible. However, pause and seek is not possible while watching, sorry!
## SubtitleSynchronizer
One of the annoying things about random subtitles is the shift from original timeline. Although modern players (i.e. PotPlayer) have a builtin option to adjust the shift, why not update the subtitle file itself?

The file SubSync.py is faulty, use SubSync.cpp instead. It takes the path to the srt file and desired timeshift, and outputs a updated srt file in the path.
