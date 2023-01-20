import openpyxl
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import datetime

path = '/home/andrew/STEVE/New_API/excel_files/Dataset_2016.xlsx'

def EPOCH_to_DATE(epoch_time):
    date_conv = datetime.datetime.fromtimestamp(epoch_time)
    return date_conv.strftime("%d-%m, %H:%M:%S")

def arrange_dates(x, y):

    return None

# Open the workbook 
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

y = []
x = []
numbs = [] 

for i in range(1, sheet_obj.max_row): #1189
    # x.append(EPOCH_to_DATE(sheet_obj.cell(row=i+1, column=1).value))
    x.append(sheet_obj.cell(row=i+1, column=1).value)
    y.append(sheet_obj.cell(row=i+1, column=2).value)

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


IT_storms = ( 
[1476139380, 1476475320],
[1457058240, 1457620560],
[1462641000, 1462978080],
[1453203960, 1453483860],
[1471662420, 1472106180],
[1477335480, 1478023800]
)
 
'''
for i in IT_storms:
    print( EPOCH_to_DATE(i[0]),',', EPOCH_to_DATE(i[1]) )
'''

plt.figure(figsize=(14, 9))
plt.scatter(x_m, y_m, color="orange")

plt.title('Ti at 275 km')
# plt.grid(True)
plt.subplots_adjust(bottom=0.162)
plt.xticks(x_m[::15], rotation='vertical')

# plt.axvline(x = 1476139380, color='r')

plt.xlabel('Epoch Time(Day-Month, Hour:Minute:Second)')
plt.ylabel('Line-of-Sight Ion Temperature [K]')

plt.plot()

plt.show()

