# THIS CODE WILL PRODUCE ION TEMPERATURE FIGURES FOR LONG-PULSE DATAFILES 
# DOWNLOADED FROM "data.amisr.com" AND THEN STRIPPED USING "Code-for-Andy-1.py"


# IMPORT THE REQUIRED LIBRARIES (DO NOT TOUCH, UNLESS ALTERING THE CODE)
import h5py as h5
import numpy as np
import matplotlib.pyplot as plt
import math
import datetime
import time


# CUSTOMIZE THE PATH TO THE DATAFILE RELATIVE TO THE CODE
path = "Andy PFISR/"

# INSERT THE NAME OF THE h5 DATAFILE YOU HAVE DOWNLOADED AND WOULD LIKE TO PLOT
filename = "TIspike20220406.005_lp_1min-fitcal.h5"

# THIS OPENS THE DATA FILE OF INTEREST
f  = h5.File(path+filename, 'r')

# BEAM PARAMETERS (E.G. ELEVATION ANGLE, AZIMUTH, ETC)
beamcodes = f['BeamCodes']
beamcodesdata = beamcodes[:,:]
beamcodesdata = beamcodesdata.astype(float)    

# EPOCH TIME
epoch = f['UnixTime']
epochData = epoch[:,:]
epochData = epochData.astype(float)    

# ALTITUDE
alt = f['Altitude']
altdata = alt[:,:]/1000.#CONVERTING FROM METERS TO KILOMETERS
altdata = altdata.astype(float)    

# PLASMA DENSITY [m-3]
ne = f['Ne']
nedata = ne[:,:,:]
nedata = nedata.astype(float)    

# ERROR IN PLASMA DENSITY [m-3]
dne = f['dNe']
dnedata = dne[:,:,:]
dnedata = dnedata.astype(float)    

# THE ION SPECIES IS SET
# 0 = O+, THE DOMINANT F-REGION ION. SOME DATAFILES OFFER, 1 = O2+, 2 = NO+ , 
# 3 = N2+ AND , 4 = N+, BUT I STRONGLY SUGGEST YOU DO NOT TOUCH THIS
ion = 0

# ION TEMPERATURE [K]
ti = f['Fits']
tidata = ti[:,:,:,ion,1]
tidata = tidata.astype(float)    

# ERROR IN ION TEMPERATURE [K]
dti = f['Errors']
dtidata = dti[:,:,:,ion,1]
dtidata = dtidata.astype(float)    

# ELECTRON TEMPERATURE [K]
te = f['Fits']
tedata = te[:,:,:,-1,1]  
tedata = tedata.astype(float)    

# ERROR IN ELECTRON TEMPERATURE [K]
dte = f['Errors']
dtedata = dte[:,:,:,-1,1]
dtedata = dtedata.astype(float)    

# LINE-OF-SIGHT ION VELOCITY [m/s]
losv = f['Fits']
losvdata = losv[:,:,:,ion,3]
losvdata = losvdata.astype(float)    

# CORRECTED GEOMAGNETIC LATITUDE [deg]
lat = f['MagneticLatitude']
latdata = lat[:,:]
latdata = latdata.astype(float)       

# CORRECTED GEOMAGNETIC LONGITUDE [deg]
long = f['MagneticLongitude']
longdata = long[:,:]
longdata = longdata.astype(float)  

# THIS CLOSES THE DATA FILE
f.close() 

# THIS CONVERTS EPOCH TIME TO UNIVERSAL TIME IN DATETIME
ut = [datetime.datetime(int(time.gmtime((epochData[t,0]+epochData[t,1])/2)[0]), # YEAR
                       int(time.gmtime((epochData[t,0]+epochData[t,1])/2)[1]), # MONTH
                       int(time.gmtime((epochData[t,0]+epochData[t,1])/2)[2]), # DAY
                       int(time.gmtime((epochData[t,0]+epochData[t,1])/2)[3]), # HOUR
                       int(time.gmtime((epochData[t,0]+epochData[t,1])/2)[4]), # MINUTE
                       int(time.gmtime((epochData[t,0]+epochData[t,1])/2)[5])) # SECOND
                       for t in range(len(epochData))]



# ERRONEOUS POINTS ARE REMOVED (COMMENT THIS OUT TO VIEW ALL MEASUREMENTS)
for tt in range(len(nedata)):
  for ii in range(len(nedata[0])):
    for jj in range(len(nedata[0,0])):
      if nedata[tt,ii,jj] < dnedata[tt,ii,jj]:
        nedata[tt,ii,jj] = np.NaN
      if tidata[tt,ii,jj] < dtidata[tt,ii,jj]:
        tidata[tt,ii,jj] = np.NaN
      if tedata[tt,ii,jj] < dtedata[tt,ii,jj]:
        tedata[tt,ii,jj] = np.NaN

# WE CYCLE THROUGH THE DIFFERENT BEAMS IN THE EXPERIMENT
for i in range(len(altdata)):
# WE FOCUS ON THE BEAM PARALLEL TO THE MAGNETIC FIELD (BEAM CODE 64157)    
  if beamcodesdata[i,0] == 64157.0:

    #WE FIND THE ION TEMPERATURE MEASURED CLOSEST TO 275 KM      
    a = abs(altdata[i,:] - 275)
    b = np.where(a == np.nanmin(a))
    Ti275 = tidata[:,i,b[0]]
    
    #WE PLOT TI
    plt.figure(figsize=(14, 7))
    plt.plot(epochData,Ti275)
    plt.title('Ti at 275 km')
    plt.grid(True)
    plt.xlabel('Epoch Time')
    plt.ylabel('Line-of-Sight Ion Temperature [K]')
    plotfile = 'Andy PFISR/275{}.png'.format(filename.split("_")[0])
    plt.savefig(plotfile)
    plt.cla()   # Clear axis
    plt.clf()   # Clear figure
    plt.close() # Close a figure window
         