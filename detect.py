import os
import pyautogui
import time
#im = pyautogui.screenshot(region=(0,0, 300, 400))

def detector(box):
   """
      the data structure is like
      data={ 'name(label)' : [[all the image names],[all the detected positions]]}
   """
   PATH='images/output/'
   input('waiting...press any key')
   data = {}
   for i in os.listdir(PATH):
       label,_=i.split('.')
       if not label in data:
          data[label]=[[i],[]]
       else:
          data[label][0].append(i)

   #Deleting the box part
   del data['box']
   #print(data)

   for i in data.keys():
      #print('detector/'+i)
      for j in data[i][0]:
         print(PATH+j)
         k=pyautogui.locateOnScreen(PATH+j,grayscale=True, confidence=.5, region=box)
         if k:
            #pyautogui.click(pyautogui.center(k))
            data[i][1].append(k)
      print('-------------------------------------------------------------')
   return data


if __name__=='__main__':
   print(detector((0,0,300,300)))

