import pyautogui
import time

time.sleep(3)

for line in open("data.txt", "r"):

    pyautogui.typewrite(line)
    
    pyautogui.press("enter")
