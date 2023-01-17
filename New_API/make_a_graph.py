import openpyxl
import matplotlib.pyplot as plt
import datetime

path = '/home/andrew/STEVE/New_API/excel_files/Dataset_2016.xlsx'

def EPOCH_to_DATE(epoch_time):
    date_conv = datetime.datetime.fromtimestamp(epoch_time)
    return date_conv.strftime("%d-%m-%Y")

# Open the workbook 
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

y = []
x = []

for i in range(1, sheet_obj.max_row): #1189
    x.append(EPOCH_to_DATE(sheet_obj.cell(row=i+1, column=1).value))
    # x.append(sheet_obj.cell(row=i+1, column=1).value)
    y.append(sheet_obj.cell(row=i+1, column=2).value)

print(sheet_obj.max_row)
print(type(sheet_obj.cell(row=2, column=1).value))

'''
print('max amount of cols: ', sheet_obj.max_row)
print('x', x)
print('y', y)
'''

plt.figure(figsize=(14, 7))
plt.scatter(x, y, color="orange")

plt.title('Ti at 275 km')
plt.grid(True)
plt.xlabel('Epoch Time')
plt.ylabel('Line-of-Sight Ion Temperature [K]')

plt.show()

