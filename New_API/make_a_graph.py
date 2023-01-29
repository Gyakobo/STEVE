import openpyxl
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import datetime
import geopy.distance

# Global Variable(s) and Function(s)
path = '/home/andrew/STEVE/New_API/excel_files/Dataset_2016.xlsx'
harsh_path_swarm_a = '/home/andrew/STEVE/New_API/Harsh_files_SWARM_A/currentYear2016-17.xlsx'
harsh_path_swarm_b = '/home/andrew/STEVE/New_API/Harsh_files_SWARM_B/currentYear2016-17.xlsx'
harsh_path_swarm_c = '/home/andrew/STEVE/New_API/Harsh_files_SWARM_C/currentYear2016-17.xlsx'

poker_flat_lat  = 65.1200
poker_flat_long = -147.4700 

def curv_distance_km(lat1, long1, lat2, long2):
    coords_1 = (lat1, long1)
    coords_2 = (lat2, long2)
    return geopy.distance.geodesic(coords_1, coords_2).km

def curv_distance_miles(lat1, long1, lat2, long2):
    coords_1 = (lat1, long1)
    coords_2 = (lat2, long2)
    return geopy.distance.geodesic(coords_1, coords_2).miles

def EPOCH_to_DATE(epoch_time):
    date_conv = datetime.datetime.fromtimestamp(epoch_time)
    return date_conv.strftime("%d-%m, %H:%M:%S")

def EPOCH_to_min(epoch_time):
    date_conv = datetime.datetime.fromtimestamp(epoch_time)
    return int(date_conv.strftime("%M"))

#################################


# Open the workbook 
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

wb_obj_swarm_a = openpyxl.load_workbook(harsh_path_swarm_a)
sheet_obj_swarm_a = wb_obj_swarm_a.active
wb_obj_swarm_b = openpyxl.load_workbook(harsh_path_swarm_b)
sheet_obj_swarm_b = wb_obj_swarm_b.active
wb_obj_swarm_c = openpyxl.load_workbook(harsh_path_swarm_c)
sheet_obj_swarm_c = wb_obj_swarm_c.active

'''
for i in range(1, sheet_obj_swarm_a):
    pass
for i in range(1, sheet_obj_swarm_b):
    pass
for i in range(1, sheet_obj_swarm_c):
    pass
'''

y_a = []
x_a = []

y_b = []
x_b = []

y_c = []
x_c = []

x = []
y = []
numbs = [] 

for i in range(1, sheet_obj.max_row): #1189
    x_slot = sheet_obj.cell(row=i+1, column=1).value 
    y_slot = sheet_obj.cell(row=i+1, column=2).value 

    for j in range(1, sheet_obj_swarm_a.max_row):
        harsh_epoch_time = sheet_obj_swarm_a.cell(row=j+1, column=1).value.timestamp()
        #harsh_te    = sheet_obj_swarm_a.cell(row=j+1, column=2).value
        harsh_long  = sheet_obj_swarm_a.cell(row=j+1, column=3).value
        harsh_lat   = sheet_obj_swarm_a.cell(row=j+1, column=4).value
        if abs(int(x_slot) - int(harsh_epoch_time)) <= (30.0 * 60.0) and curv_distance_km(harsh_lat, harsh_long, poker_flat_lat, poker_flat_long) <= 500:
            x_a.append(x_slot)
            y_a.append(y_slot)

    for j in range(1, sheet_obj_swarm_b.max_row):
        harsh_epoch_time = sheet_obj_swarm_b.cell(row=j+1, column=1).value.timestamp()
        #harsh_te    = sheet_obj_swarm_b.cell(row=j+1, column=2).value
        harsh_long  = sheet_obj_swarm_b.cell(row=j+1, column=3).value
        harsh_lat   = sheet_obj_swarm_b.cell(row=j+1, column=4).value
        if abs(int(x_slot) - int(harsh_epoch_time)) <= (30.0 * 60.0) and curv_distance_km(harsh_lat, harsh_long, poker_flat_lat, poker_flat_long) <= 500:
            x_b.append(x_slot)
            y_b.append(y_slot)

    for j in range(1, sheet_obj_swarm_c.max_row):
        harsh_epoch_time = sheet_obj_swarm_c.cell(row=j+1, column=1).value.timestamp()
        #harsh_te    = sheet_obj_swarm_a.cell(row=j+1, column=2).value
        harsh_long  = sheet_obj_swarm_c.cell(row=j+1, column=3).value
        harsh_lat   = sheet_obj_swarm_c.cell(row=j+1, column=4).value
        if abs(int(x_slot) - int(harsh_epoch_time)) <= (30.0 * 60.0) and curv_distance_km(harsh_lat, harsh_long, poker_flat_lat, poker_flat_long) <= 500:
            x_c.append(x_slot)
            y_c.append(y_slot)
'''
for i in range(len(x)):
    numbs.append([x[i], y[i]])
def lambda_(element):
    return element[0] 
numbs = sorted(numbs, key = lambda_)

y_m = []
x_m = []
for i in range(len(x)):
    x_m.append( EPOCH_to_DATE(numbs[i][0]) )
    y_m.append( numbs[i][1] )
'''

IT_storms = ( 
#[1476139380, 1476475320],
[1457058240, 1457620560],
[1462641000, 1462978080],
[1453203960, 1453483860],
#[1471662420, 1472106180],
#[1477335480, 1478023800]
)
 

plt.figure(figsize=(14, 9))

# A + B + C
'''
for i in range(len(x)):
    numbs.append([x[i], y[i]])
def lambda_(element):
    return element[0] 
numbs = sorted(numbs, key = lambda_)

y_m = []
x_m = []
for i in range(len(x)):
    x_m.append( EPOCH_to_DATE(numbs[i][0]) )
    y_m.append( numbs[i][1] )
plt.scatter(x_m, y_m, color="orange")
plt.xticks(x_m, rotation='vertical')
'''


# A, B, C
plt.scatter(x_a, y_a, color="orange", label="SWARM A")

plt.scatter(x_b, y_b, color="green", label="SWARM B")

plt.scatter(x_c, y_c, color="blue", label="SWARM C")
plt.xticks(rotation='vertical')

#plt.grid(True)
#plt.xticks(x_m[::15], rotation='vertical')

plt.title('Ti at 275 km')
plt.subplots_adjust(bottom=0.162)

for i in IT_storms: 
    plt.axvline(x = i[0], color='r')
    plt.axvline(x = i[1], color='g')

plt.xlabel('Epoch Time(Day-Month, Hour:Minute:Second)')
plt.ylabel('Line-of-Sight Ion Temperature [K]')

plt.plot()

plt.show()

