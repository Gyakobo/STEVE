import h5py
from numpy import NaN, Inf, arange, isscalar, asarray, array
import numpy as np
import sys
import matplotlib.pyplot as plt
from math import *

# EVIl Peak finding function
from endolith_peakdet import *



# Essential Variables ######################
file_name_0   = "/home/andrew/STEVE/madrigalWeb/madrigalWeb/downloads/pfa070301.002.hdf5"
file_name_1   = "/home/andrew/STEVE/madrigalWeb/madrigalWeb/downloads/pfa070327.002.hdf5"
file_name_2   = "/home/andrew/STEVE/madrigalWeb/madrigalWeb/downloads/pfa070401.002.hdf5"

elevation_angle = ((90.0+77.5)*pi) / 180.0
range_names = (
    102.2,
    138.17,
    174.15,
    210.12,
    246.1,
    282.07,
    318.05,
    354.02,
    390.0,
    425.97,
    461.95,
    497.92,
    533.9,
    569.87,
    605.85,
    641.82,
    677.8
)
###########################################



# Checks whether the argument is a NaN
def isNaN(num):
    if float('-inf') < float(num) < float('inf'):
        return False
    else:
        return True


# Calculates altitude from the given ranges
def calc_alt(a, b, alpha):
    return sqrt(a**2 + b**2 - 2 * a * b * cos(alpha)) - a


# Gets the peaks and the given plunges of a given array
# Dr.Gareth asked to change the THRESHOLD
def get_peaks(data, file, THRESHOLD = 2):
    m_data = []
    numb_of_nans = 0
    
    ''' 
    for i in range(0, len(data)):
        if not isNaN(data[i]):
            numb_of_nans += 1
            m_data.append(data[i])
    data = m_data
    '''

    mean    = sum(data) / len(data)
    std_dev = (sum( [ (val-mean)**2 for val in data ] )/ (len(data)-1))**0.5
    peaks, plunges = peakdet(data, THRESHOLD*std_dev)

    return array(peaks)[:,0], array(peaks)[:,1], array(plunges)[:,0], array(plunges)[:,1], std_dev, mean


file    = np.array(h5py.File(file_name_0, 'r').file.get('Data').get('Table Layout'))
file_1  = np.array(h5py.File(file_name_1, 'r').file.get('Data').get('Table Layout'))
file_2  = np.array(h5py.File(file_name_2, 'r').file.get('Data').get('Table Layout'))
dataset = np.append(file, file_1, axis = 0)
dataset = np.append(dataset, file_2, axis = 0)

#print(dataset)


# Various altitudes #################
alt_names = []
for i in range(0, len(range_names)):
    alt_names.append(calc_alt(6378.1, range_names[i], elevation_angle))

#inc     = 33269
inc     = 0 
#new_i   = inc

ion_temp = [None] * 17
for i in range(0, len(ion_temp)):
    ion_temp[i] = []
######################################





# Basic or even main interval
days = 4
hours_24 = 24
######################################



# Calculate all altitudes 
for i in range(0, (hours_24*days) *4): #Needs to be 8
    for altitudes in range(0, 17):     
        ion_temp[altitudes].append(dataset[inc + (i+0)*17 + altitudes][11])

        #new_i += 17
# Choose your range
choose_range = 5

peaks_x, peaks_y, plunges_x, plunges_y, std_dev, mean = get_peaks(ion_temp[choose_range], dataset, THRESHOLD=3.5)

for i in range(0, len(peaks_x)):
    print(file[i])


x = np.linspace(0, len(ion_temp[choose_range]))
######################################




# Plot a graph ######################
end_index = len(ion_temp)
for altitudes in range(choose_range, choose_range+1): # You can put the "end_index here"     
    plt.plot(ion_temp[altitudes], label='Alt='+str(alt_names[altitudes])[:5] + ', Range = ' + str(range_names[choose_range]))
######################################





# Print peaks
print('\n')
print("Print peaks")
print(peaks_x)

plt.scatter(peaks_x, peaks_y, color="blue")
plt.scatter(plunges_x, plunges_y, color="red")

# The standard deviation line 
plt.plot([std_dev]*len(ion_temp[choose_range]), linestyle="--", label='Standard deviation = ' + str(std_dev)[:5])
plt.plot([mean]*len(ion_temp[choose_range]), linestyle="--", label='Mean = ' + str(mean)[:5])

print('\n')
print('std_dev = ' + str(std_dev))

plt.legend(loc='best')
plt.xlabel('Take each x increment in 15[min] intervals')
plt.ylabel('Ti [K]')
plt.show()

