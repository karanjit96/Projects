
import pyautogui

pyautogui.PAUSE=5 
try:
    while (1):
            pyautogui.click(duration=1)    
            

except KeyboardInterrupt:
    print('Quitting')
