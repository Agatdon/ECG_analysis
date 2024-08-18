import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import find_peaks
from calculate_intervals import calculate_intervals
from plots import *

''' PART 1 R-R ANALYSIS'''

# RAED DATA
f = open("Nick-3-EKG_adjusted.txt", "r")
samples = len(f.read().splitlines())
print("Found " + str(samples) + " lines in the dataset")

sampleFrequency = 250  # Herz
sampleDuration = 1 / sampleFrequency

duration = samples / sampleFrequency
print("As in " + str(duration) + " seconds sampled")

# READ TO DATA FRAME
ecgdata = pd.read_csv("Nick-3-EKG_adjusted.txt", sep='\t', index_col=None)
# CHANDE TO TIME [S]
ecgdata.index = ecgdata.index.map(lambda x: x / sampleFrequency)

# DRAWING
plotChan(ecgdata.loc[:50], "CH1", grid=True)

# CONWERT TO TABLE
channel_data = ecgdata['CH1'].values

# FIND LOCAL MAXIMUM
peaks, _ = find_peaks(channel_data)

# THRESHOLDS
x = 0.35
y=0.29

# FILTRACION
filtered_peaks = peaks[channel_data[peaks] > x ]


#print("Indeksy lokalnych maksimów powyżej wartości", x, ":", filtered_peaks)
#print("Wartości lokalnych maksimów powyżej wartości", x, ":", channel_data[filtered_peaks])

# ADD PEAKS TO DROWING
plt.plot(ecgdata.index[filtered_peaks], channel_data[filtered_peaks], "ro")

# AXIS LIMITATION
plt.xlim(0, 50)

# SHOW DRAWING
plt.show()

# CALCULATION OF R-R INTERVALS
intervals = calculate_intervals(filtered_peaks, ecgdata.index)

#print("Odstępy czasowe pomiędzy kolejnymi lokalnymi maksimami:", intervals)

STD_channel=np.std(intervals)
print("Odychylenie standardowe R-R:" + np.array2string(STD_channel))
