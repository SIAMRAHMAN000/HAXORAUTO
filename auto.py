import pyautogui
import time

time.sleep(10)

for line in open("data.txt", "r"):

    pyautogui.typewrite(line)
    
    pyautogui.press("enter")
