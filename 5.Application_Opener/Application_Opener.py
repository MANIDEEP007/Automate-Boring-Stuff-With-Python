#Author: Paduchuri Manideep

#To Open the Specified Processes in txt file
import os
import time

'''
Give Exe or File in double quotes and have r letter before that
to allow spaces or backslash in Paths
Feel free to try other types of files/exe and use it
This is purely for educational and Personal use
'''

Apps_List = [
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", #Chrome
    r"C:\Windows\notepad.exe", #Notepad
    r"C:\Program Files\Python37\Lib\idlelib\idle.pyw", #IDLE
    r"D:\Python Socket Module.docx", #Word Document
    r"D:\Manideep.xlsx", #Excel
    r"C:\Users\Manideep\Downloads\Manideep_Paduchuri.pdf", #PDF Document
    r"C:\Users\Manideep\Downloads\1.Notes\32.Data+types+notes.html", #HTML File
    ]

#Open Each Exe or File with 5seconds interval between them
for each_app in Apps_List:
    os.popen(each_app)
    time.sleep(5)
