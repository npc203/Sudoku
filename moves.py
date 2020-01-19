import pyautogui
import pygetwindow as gw


#pyautogui.moveTo(x,y, duration = 0)
#pyautogui.click(x,y) 

'''
w=gw.getWindowsWithTitle('Remote Control - Redmi Go')[0]
print(w.topleft.x,w.topleft.y)
pyautogui.moveTo(w.topleft.x,w.topleft.y, duration = 0)
pyautogui.moveTo(1169,617, duration = 0)
#The place where i record the coords is (790 107)
'''


def convert(string):
    """Function takes tuple strings as input and returns tuples"""
    return tuple(int(i) for i in string.replace('(','').replace(')','').split(','))
    


#Parsing
arr=[]
with open('coordinates.txt','r') as f:
    lines=f.readlines()
op=0
for i in range(9):
    tmp=[]
    for j in range(9):
       tmp.append(convert(lines[op].replace('\n','')))
       op+=1
    arr.append(tmp)
w=gw.getWindowsWithTitle('Remote Control - Redmi Go')[0]
with open('process.txt','w+') as f:
    for i in arr:
        for j in i:
            print(j[0],j[1])
            f.write('('+str(j[0]-w.topleft.x)+','+str(j[1]-w.topleft.y)+')\n')




