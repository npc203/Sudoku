import pyautogui
import pygetwindow as gw


#pyautogui.moveTo(x,y, duration = 0)
#pyautogui.click(x,y) 

'''
w=gw.getWindowsWithTitle('Remote Control - Redmi Go')[0]
print(w.topleft.x,w.topleft.y)
pyautogui.moveTo(w.topleft.x,w.topleft.y, duration = 0)
pyautogui.moveTo(1169,617, duration = 0)
'''


def move(string):
    """Function takes tuple strings as input and moves to the approriate position"""
    cod=(int(i) for i in string.replace('(','').replace(')','').split(',')])
    pyautogui.moveTo(cod[0],cod[1], duration = 0.01)
    


#Parsing
arr=[]
with open('coordinates.txt','r') as f:
    lines=f.readlines()
op=0
for i in range(9):
    tmp=[]
    for j in range(9):
       tmp.append(lines[op].replace('\n',''))
       op+=1
    arr.append(tmp)





