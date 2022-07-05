import h5py
from numpy import NaN, Inf, arange, isscalar, asarray, array 
import numpy as np
import sys
import matplotlib.pyplot as plt
from   scipy.signal import find_peaks
from   math import * 


# EVIL Peak finding function
from endolith_peakdet import *

file_name = "data.hdf5"

def isNaN(num):
    if float('-inf') < float(num) < float('inf'):
        return False
    else:
        return True



def get_peaks(data, THRESHOLD=2):
    m_data = []

    numb_of_nans = 0
    
    for i in range(0, len(data)):
        if not isNaN(data[i]):
            numb_of_nans += 1
            m_data.append(data[i])        
    data = m_data
    

    mean    = sum(data) / len(data)
    std_dev = (sum( [ (val-mean)**2 for val in data ] )/ (len(data)-1))**0.5

    peaks, plunges = peakdet(data, THRESHOLD*std_dev) 
    
    '''
    for i in range(1, len(data)-1):
        if (data[i] > data[i-1] and data[i] > data[i+1]):
            if (abs(data[i] - mean) > THRESHOLD*std_dev):
                peaks.append(i)
    '''

    #peaks_x, _ = find_peaks(data, prominence=THRESHOLD*std_dev)

    print('\n')
    print('number of nans = ' + str(numb_of_nans) + '\n')

    #type(peaks)

    return array(peaks)[:,0], array(peaks)[:,1], array(plunges)[:,0], array(plunges)[:,1], std_dev, mean








def calc_alt(a, b, alpha):
    return sqrt(a*a + b*b - 2*a*b*cos(alpha)) - a

elevation_angle = ((90.0+77.5)*pi)/180.0

range_names = [
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
]

with h5py.File(file_name, 'r') as file:
    keys = list(file.keys())

    # List keys
    print("Keys: %s" % keys)

    data    = file.get('Data').get('Table Layout')
    dataset = np.array(data)


    # Various altitudes
    alt_names = []
    for i in range(0, len(range_names)):
        alt_names.append(calc_alt(6378.1, range_names[i], elevation_angle))

    print('List of altitudes')
    print(alt_names)

    # List entire dataset
    # print(dataset[5:])

    inc = 33269
    new_i = inc

    # Need to add 17 to get to the next 15 min increment

    ion_temp = [None] * 17 
    for i in range(0, len(ion_temp)):
        ion_temp[i] = []


    hours_24 = 24
    days = 6

    for i in range(0, (hours_24*days) *4): #Needs to be 8
        for altitudes in range(0, 17):     
            #ion_temp[altitudes].append(dataset[new_i+altitudes][21])
            ion_temp[altitudes].append(dataset[inc + (i+0)*17 + altitudes][21])

        #new_i += 17

    # Choose your range
    choose_range = 5 

    # Find peaks    
    # peaks, _ = find_peaks(ion_temp[choose_range], height=0)
    peaks_x, peaks_y, plunges_x, plunges_y, std_dev, mean = get_peaks(ion_temp[choose_range], THRESHOLD=3.5)

    x = np.linspace(0, len(ion_temp[choose_range]))


    # Plot a graph
    end_index = len(ion_temp)
    for altitudes in range(choose_range, choose_range+1): # You can put the "end_index here"     
        plt.plot(ion_temp[altitudes], label='Alt='+str(alt_names[altitudes])[:5] + ', Range = ' + str(range_names[choose_range]))

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


