import pyautogui
import time
#screenWidth, screenHeight = pyautogui.size()

pyautogui.moveTo(605, 897, duration=1.10)
pyautogui.click(605, 897, button='left')
pyautogui.moveTo(1073, 668, duration=1.05)
pyautogui.click(1073, 668, button='left')

while True:

        
    pyautogui.press('F11')

    time.sleep(85)

    pyautogui.press('F11')

    time.sleep(75)

    pyautogui.press('F11')

    time.sleep(85)

    pyautogui.press('F11')

    time.sleep(60)
    
    pyautogui.typewrite('adori mas flam'); pyautogui.press('enter')

    time.sleep(120)




