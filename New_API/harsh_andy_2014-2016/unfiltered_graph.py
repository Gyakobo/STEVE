import openpyxl
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import datetime
# import geopy.distance
# import os
from openpyxl import Workbook
import openpyxl
import numpy as np


# Global Variable(s) and Function(s)
path    = '/home/andrew/STEVE/New_API/excel_files/Dataset_2014-2016.xlsx'

def EPOCH_to_DATE(epoch_time):
    date_conv = datetime.datetime.fromtimestamp(epoch_time)
    return date_conv

def scatter_hist(x, y, ax, ax_histx, ax_histy):
    x = np.array(x)
    y = np.array(y)

    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    ax.scatter(x, y)

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')


def subtract_time(hours, minutes):
    time_in_minutes = hours*60 + minutes

    time_in_minutes -= (7*60+45)

    if (time_in_minutes < 0):
        print("original hour:", time_in_minutes // 60, "original minutes:", time_in_minutes % 60) 
        time_in_minutes += 24*60
        print("fomatted hour:", time_in_minutes // 60, "formatted minutes:", time_in_minutes % 60, end="\n\n") 
    
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
    # os.system('clear')
    # print("Iteration:", i, "/", sheet_obj.max_row)
    
    date = EPOCH_to_DATE(sheet_obj.cell(row=i+1, column=1).value) 
    y_slot = sheet_obj.cell(row=i+1, column=2).value 

    if (y_slot <= 20000):        
        year    = date.year #sheet_obj_swarm_a.cell(row=j+1, column=1).value
        time    = date.time()
 
        hours, minutes = subtract_time(time.hour, time.minute)
        # alaska_datetime = datetime.datetime(
        #        year=2000, month=1, day=1, hour=hours, minute=minutes,
        #        second=time.second, microsecond=time.microsecond)
 
        x.append(hours + minutes / 60.0)
        y.append(y_slot)


pre_noon        = 0
post_midnight   = 6
post_noon       = 12
pre_midnight    = 18

day_time = [ post_midnight, pre_noon, post_noon, pre_midnight ]

fig = plt.figure(figsize=(14, 9))

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

'''
gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)
# Create the Axes.
ax = fig.add_subplot(gs[1, 0])
ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
# Draw the scatter plot and marginals.
scatter_hist(x, y, ax, ax_histx, ax_histy)
'''
