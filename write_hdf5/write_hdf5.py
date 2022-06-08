import h5py
import numpy as np
import matplotlib as plt

matrix1 = np.random.random(size= (10, 10))
matrix2 = np.random.random(size= (10, 10))

# create_dataset(name(string value), shape=None, dtype=None, data=None, **kwds)

with h5py.File('example_hdf5_data.hdf5', 'w') as hdf:
    hdf.create_dataset('dataset1', data = matrix1)
    hdf.create_dataset('dataset2', data = matrix2)


