import h5py
import numpy as np
import matplotlib.pyplot as plt
from   scipy.signal import find_peaks

file_name = "data.hdf5"

with h5py.File(file_name, 'r') as file:
    keys = list(file.keys())

    # List keys
    print("Keys: %s" % keys)

    data = file.get('Data').get('Table Layout')
    dataset = np.array(data)

    # List entire dataset
    #print(dataset[5:])

    inc = 33269 

    ranges = [None] * 24 * 4
    for i in range(0, len(ranges)):
        ranges[i] = []

    # Measure the Ti by T at range1=102.2
    for i in range(inc, inc+len(ranges)):
        for j in range(0, len(ranges)):
            ranges[i][j].append(dataset[inc+j][21]) 
        
        '''
        Range1_temp.append(dataset[inc][21])
        Range2_temp.append(dataset[inc+1][21])
        Range3_temp.append(dataset[inc+2][21])
        Range4_temp.append(dataset[inc+3][21])
        Range5_temp.append(dataset[inc+4][21])
        Range6_temp.append(dataset[inc+5][21])
        Range7_temp.append(dataset[inc+6][21])
        Range8_temp.append(dataset[inc+7][21])
        Range9_temp.append(dataset[inc+8][21])
        Range10_temp.append(dataset[inc+9][21])
        Range11_temp.append(dataset[inc+10][21])
        Range12_temp.append(dataset[inc+11][21])
        '''
        inc += 17

        #print(str(dataset[inc][21]) + ', index = ' + str(inc)  + '\n')

    plt.plot(ranges[0], label="range1=102.2")
    
    '''    
    plt.plot(Range2_temp, label="range2=138.17")
    plt.plot(Range3_temp, label="range3=174.15")
    plt.plot(Range4_temp, label="range4=210.12")
    plt.plot(Range5_temp, label="range5=246.1")
    plt.plot(Range6_temp, label="range6=282.07")
    plt.plot(Range7_temp, label="range7=318.05")
    plt.plot(Range8_temp, label="range8=354.02")
    '''

    plt.xlabel('technically time in 15 min intervals')
    plt.ylabel('Ti, k')
    plt.title('Plot with their subsequent ranges and altitudes')
    plt.show()
