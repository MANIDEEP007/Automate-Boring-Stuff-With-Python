import webbrowser
from os import strerror
import sys
import time

#Check for the File - Make Sure file Exists in same path of code
try:
    file  = open("URLs.txt")
except IOError as exc:
    '''
    Using errno and os function strerror
    We can Print the descripion of the error
    '''
    print("Error is",strerror(exc.errno))
    exit(0)

#File Exists - Read the data(URL's)
urls = file.readlines()

#Opening all URL's in file in System Default browser
for each in urls:
    '''
    new=2 ==> Opens in New tab if browser is open
    Else opens browser for first time. Then opens
    succeding ones in New Tabs
    '''
    if webbrowser.open(each,new=2):
        print("Successfully Opened ", each)
    else:
        print("Failed to Open ",each)
    #Sleep for 5 seconds before opening new URL
    time.sleep(5)
