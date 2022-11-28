import openpyxl
import matplotlib.pyplot as plt

path = '/home/andrew/STEVE/New_API/excel_files/Dataset_2014.xlsx'

# Open the workbook 
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

y = []
x = []

for i in range(sheet_obj.max_row):
    x.append(sheet_obj.cell(row=i+2, column=1).value)
    y.append(sheet_obj.cell(row=i+2, column=2).value)

'''
print('max amount of cols: ', sheet_obj.max_row)
print('x', x)
print('y', y)
'''

plt.figure(figsize=(14, 7))
plt.scatter(x[:-1], y[:-1], color="orange")

plt.title('Ti at 275 km')
plt.grid(True)
plt.xlabel('Epoch Time')
plt.ylabel('Line-of-Sight Ion Temperature [K]')

plt.show()

