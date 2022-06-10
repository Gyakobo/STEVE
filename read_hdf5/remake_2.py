import h5py
import numpy as np
import matplotlib.pyplot as plt
from   scipy.signal import find_peaks
from   math import * 

file_name = "data.hdf5"
    
def calc_alt(a, b, alpha):
    return sqrt(a*a + b*b - 2*a*b*cos(alpha)) - a

elevation_angle = 77.5

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


    for i in range(0, 24*4):
        for altitudes in range(0, 17):     
            ion_temp[altitudes].append(dataset[new_i+altitudes][21])

        new_i += 17


    # Find peaks    
    peaks, _ = find_peaks(ion_temp[0], height=0)


    # Plot a graph
    end_index = len(ion_temp)
    for altitudes in range(0, end_index): # You can put the "end_index here"     
        plt.plot(ion_temp[altitudes], label='Alt='+str(alt_names[altitudes]))

    # Print peaks
    print("Print peaks")
    print(peaks)

    plt.plot(peaks, np.array(ion_temp[0])[peaks], "x")

    plt.xlabel('Take each x increment in 15[min] intervals')
    plt.ylabel('Ti [K]')
    plt.show()


