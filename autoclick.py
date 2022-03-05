
import pyautogui
global pause
pause=5
pyautogui.PAUSE=pause 
print('Running')
global counter
counter =0
try:
    while (1):
        
        counter +=1
        pyautogui.click(duration=1)    
            

except KeyboardInterrupt:
    print('Quitting')
    print('program ran for: {x} mins'.format(x=((counter*pause)/60)))
    
  
