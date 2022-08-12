import h5py as h5
import os 
import urllib

from urllib.request import urlopen
from urllib.request import urlretrieve
import cgi
from urllib.error import HTTPError

"""
INPUT PARAMETERS
"""


f1 = open('inputfile.txt', 'r') 
files = f1.read().splitlines()
f1.close() 



for t in range(len(files)):
  filename = str(files[t])
  filename1 = filename.split("_")[0]


  url = 'https://data.amisr.com/database/dbase_site_media/PFISR/Experiments/'+filename1+'/DataFiles/'+filename

  filesexists = -30
  try:
    urllib.request.urlretrieve(url, 'Andy PFISR/'+filename)
  except urllib.error.HTTPError as err:
    print(err.code)
    filesexists = err.code


  if filesexists == -30:  

    fs = h5.File('Andy PFISR/'+filename, 'r')
    fd = h5.File('Andy PFISR/TIspike'+filename, 'w')


    for a in fs.attrs:
      fd.attrs[a] = fs.attrs[a]

    for d in fs:
      if d != 'Calibration' and d != 'MSIS' and d != 'NeFromPower' and d != 'ProcessingParams' and d != 'Site' and d != 'FittedParams/Fits': 
        if d == 'FittedParams':
              fs.copy('FittedParams/Ne',fd)
              fs.copy('FittedParams/dNe',fd)
              fs.copy('FittedParams/Fits',fd)#:,:,:,0,3
              fs.copy('FittedParams/Errors/',fd)
              fs.copy('FittedParams/FitInfo',fd)

        if d == 'Geomag':
              fs.copy('Geomag/MagneticLatitude',fd)
              fs.copy('Geomag/MagneticLongitude',fd)
              fs.copy('Geomag/Latitude',fd)
              fs.copy('Geomag/Longitude',fd)
              fs.copy('Geomag/Altitude',fd)

        if d == 'Time':
              fs.copy('Time/Day',fd)
              fs.copy('Time/Month',fd)
              fs.copy('Time/Year',fd)
              fs.copy('Time/dtime',fd)
              fs.copy('Time/UnixTime',fd)
              fs.copy('Time/doy',fd)

 
        if d == 'BeamCodes':
          fs.copy('BeamCodes',fd)

    fs.close()
    fd.close()
    os.remove('Andy PFISR/'+filename)









