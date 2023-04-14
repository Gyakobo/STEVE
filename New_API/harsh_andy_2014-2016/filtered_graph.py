import openpyxl
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import datetime
import geopy.distance
import os
from openpyxl import Workbook
import openpyxl


# Global Variable(s) and Function(s)
path_filtered      = './2014-2016_filtered.xlsx'

# Main path
path = path_filtered

def EPOCH_to_DATE(epoch_time):
    date_conv = datetime.datetime.fromtimestamp(epoch_time)
    return date_conv


def subtract_time(hours, minutes):
    time_in_minutes = hours*60 + minutes

    time_in_minutes -= (7*60+45)

    if (time_in_minutes < 0): time_in_minutes += 24*60
    
    hours   = time_in_minutes // 60
    minutes = time_in_minutes % 60

    # print("hours:", hours, "minutes:", minutes)

    return hours, minutes
###################################################

# Open the workbook 
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

y = []
x = []


for i in range(1, sheet_obj.max_row): # sheet_obj.max_row
    os.system('clear')
    print("Iteration:", i, "/", sheet_obj.max_row)
    
    date = EPOCH_to_DATE(sheet_obj.cell(row=i+1, column=2).value) 
    y_slot = sheet_obj.cell(row=i+1, column=6).value 

    if (y_slot <= 20000):        
        year    = date.year 
        time    = date.time()
 
        hours, minutes = subtract_time(time.hour, time.minute)
        alaska_datetime = datetime.datetime(
                year=2000, month=1, day=1, hour=hours, minute=minutes,
                second=time.second, microsecond=time.microsecond) 
 
        x.append(alaska_datetime)
        y.append(y_slot)


pre_noon        = datetime.datetime(2000, 1, 1, 0, 0, 0)
post_midnight   = datetime.datetime(2000, 1, 1, 6, 0, 0)
post_noon       = datetime.datetime(2000, 1, 1, 12, 0, 0)
pre_midnight    = datetime.datetime(2000, 1, 1, 18, 0, 0)
day_time = [ post_midnight, pre_noon, post_noon, pre_midnight ]

plt.figure(figsize=(14, 9))

plt.scatter(x, y, color="orange", label="IT: " + str(len(y)))

plt.grid(True)

plt.title('Ti at 275 km')
plt.subplots_adjust(bottom=0.162)

for i in day_time: 
    plt.axvline(x = i, color='r')

plt.xlabel("IT: " + str(sheet_obj.max_row) + " points found")
plt.ylabel('Line-of-Sight Ion Temperature [K]')

plt.legend()
plt.plot()

plt.show()