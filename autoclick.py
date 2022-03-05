
import pyautogui
import time
#finding the size of screen
print(pyautogui.size())

#this code moves the mouse at given duration
#pyautogui.moveTo(-100,-100,duration=1)
while(1):
    pyautogui.click(None,None,duration=1)
    time.sleep(60)