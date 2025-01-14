import pyautogui, time
time.sleep(5); f = open('Sytnex.txt', "r")
for line in f:
    pyautogui.typewrite(line)
    pyautogui.press('enter')

