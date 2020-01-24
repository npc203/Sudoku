from backend import solve
from detect import detector as dt
from moves import move
import pygetwindow as gw
import pyautogui as pg

"""
   board details:
      box
         width :45
         height:45
"""
#Identify board and it's items
w=gw.getWindowsWithTitle('Remote Control - Redmi Go')[0]
win=(w.left,w.top,w.right,w.bottom)
print('Window found at:',win)
data=dt(win)



#Solve the board and mark the items in board
print(data)
