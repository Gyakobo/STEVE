# Detecting abrupt changes in a graph 
So there were a couple of methods to use when final the quick and abrupt spikes. I've so far uncovered the aforementioned "Change Point Detection"(Not a well-known algorithm, but works fine) and the "Peak Signal Detection in realtime timeseries data", and so on.

Change point detection (or CPD) detects abrupt shifts in time series trends (i.e. shifts in a time series’ instantaneous velocity), that can be easily identified via the human eye, but are harder to pinpoint using traditional statistical approaches. CPD is applicable across an array of industries, including finance, manufacturing quality control, energy, medical diagnostics, and human activity analysis.

CPD is great for the following use cases:
1. Detecting anomalous sequences/states in a time series
1. Detecting the average velocity of unique states in a time series
1. Detecting a sudden change in a time series state in real time


# Color Grading Ranges 

1) 1300 - 1240
#890000 - #d90000
(137, 0, 0) - (217, 0, 0)


2) 1240 - 1180
#f80000 - #ff5300
(248, 0, 0) - (255, 83, 0)


3) 1180 - 1120
#ff5f00 - #f0ad00
(255, 95, 0) - (240, 173, 0)


4) 1120 - 1060
#ffc500 - #dfff1d
(255, 197, 0) - (223, 255, 29)


5) 1060 - 1000
#bee626 - #7aff82
(190, 230, 38) - (190, 230, 38)


6) 1000 - 940
#6eff8f - #15ffe7
(110, 255, 143) - (21, 255, 231)


7) 940 - 880
#07dbd2 - #00b2ff
(7, 219, 210) - (0, 178, 255)


8) 880 - 820
#00a1ff - #004dff
(0, 161, 255) - (0, 77, 255)


9) 820 - 760
#003cff - #0000ec
(0, 60, 255) - (0, 0, 236)


10) 760 - 700
#0000db - #000069
(0, 0, 219) - (0, 0, 105)

