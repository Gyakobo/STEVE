from fileinput import filename
from tkinter import *
import os
import subprocess
import datetime

# GUI Prerequisites #############
root = Tk()
root.title("GUI Version - LISA")

root.geometry("300x200") # Size of Window
#################################

# Dynamic Terminal ##############
my_str = StringVar() 

l1 = Label(root, textvariable=my_str)
l1.grid(row=1, column=0)

def change_name(k):
    my_str.set("Working with: " + str(k))
    #os.system("sudo Code-for-Andy-2.py " + str(k))
    #subprocess.call("sudo Code-for-Andy-2.py " + str(k), shell=True)
    p = subprocess.Popen(['python3', 'Code-for-Andy-2.py', str(k)])
    print("##############################")
    print("sudo Code-for-Andy-2.py " + str(k))
    print("##############################")
#################################


# folder path
dir_path = "/home/andrew/PFISR_data/" 

# list to store names of files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

#print(res)

for file_name in res:
    my_str.set("Working with: " + file_name)
    subprocess.call(['python3', 'Code-for-Andy-2.py', file_name])




for j in range(len(res)):
    e = Button(root, text=res[j], command=lambda k=res[j]:change_name(k))
    #e.invoke()
    e.grid(row=j+2, column=0, padx=2, pady=2)

root.mainloop()

