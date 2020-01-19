from pynput import keyboard,mouse

def full_box(file):
   COMBINATION = {keyboard.Key.ctrl_l}
   # The currently active modifiers
   current = set()
   global value
   global coords
   coords = list()
   value=False
   def on_press(key):
       global value
       if key in COMBINATION:
           current.add(key)
           if all(k in current for k in COMBINATION):
               value=True
       if key == keyboard.Key.esc:
           keyb.stop()
           mou.stop()

   def on_release(key):
       global value
       try:
           current.remove(key)
           coords=[]
           value=False
       except KeyError:
           pass

   def on_click(x, y, button, pressed):
       global value
       global coords
       if pressed and button==mouse.Button.left:
           if value:
               print('({},{})\n'.format(x,y))
               with open(file,'a+') as f:
                  f.write('({},{})\n'.format(x,y))
               
   with keyboard.Listener(on_press=on_press) as keyb:
    with mouse.Listener(on_click=on_click) as mou:
        print('begin')
        keyb.join()
        mou.join()
   return coords
        

if __name__=="__main__":
   full_box('coordinates.txt')
 
