import h5py
import numpy as np
import matplotlib.pyplot as plt
from   scipy.signal import find_peaks

file_name = "data.hdf5"

alt_name = [
    "range=102.2", 
    "range=138.17", 
    "range=174.15", 
    "range=210.12", 
    "range=246.1", 
    "range=282.07", 
    "range=318.05", 
    "range=354.02", 
    "range=390.0", 
    "range=425.97", 
    "range=461.95", 
    "range=497.92", 
    "range=533.9", 
    "range=569.87", 
    "range=605.85", 
    "range=641.82", 
    "range=677.8", 
]


with h5py.File(file_name, 'r') as file:
    keys = list(file.keys())

    # List keys
    print("Keys: %s" % keys)

    data    = file.get('Data').get('Table Layout')
    dataset = np.array(data)

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
    
    for altitudes in range(0, len(ion_temp)):     
        plt.plot(ion_temp[altitudes], label=alt_name[altitudes])

    plt.xlabel('Take each x increment in 15[min] intervals')
    plt.ylabel('Ti, [K]')
    plt.show()


