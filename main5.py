# 自动化操作键鼠 pr 
# pyinstaller D:\pythonxiangmu\zidonghua\main5.py --onefile --icon=tubiao.ico



import pyautogui
import time
import keyboard

# 定义一个执行鼠标点击和键盘输入的函数
def click_and_type(x, y, text):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.write(str(text))
    time.sleep(0.3)

#判断按下了ctrl+alt+1或者ctrl+alt+2，如果前者按下，执行下面的代码，如果后者按下，退出程序
while True:
    if keyboard.is_pressed('ctrl+alt+1'):#4
        click_and_type(139, 158, 1628)
        click_and_type(198, 158, -1014)
        click_and_type(146, 181, 284)
        click_and_type(147, 455, 41.2)
        click_and_type(141, 475, 87.4)
        click_and_type(135, 495, 44.8)
        click_and_type(134, 517, 6.8)
        pyautogui.press('enter')
    if keyboard.is_pressed('ctrl+alt+2'):#5
        click_and_type(139, 158, 1577.6)
        click_and_type(198, 158, -1014)
        click_and_type(146, 181, 284)
        click_and_type(147, 455, 40.6)
        click_and_type(141, 475, 87.4)
        click_and_type(135, 495, 44.1)
        click_and_type(134, 517, 7.3)
        pyautogui.press('enter')
    if keyboard.is_pressed('ctrl+alt+3'):#6
        click_and_type(139, 158, 1502.6)
        click_and_type(198, 158, -1014)
        click_and_type(146, 181, 284)
        click_and_type(147, 455, 39.0)
        click_and_type(141, 475, 87.4)
        click_and_type(135, 495, 42.5)
        click_and_type(134, 517, 7.3)
        pyautogui.press('enter')
    if keyboard.is_pressed('ctrl+alt+4'):#4-1
        click_and_type(139, 158, 1628)
        click_and_type(198, 158, -1014)
        click_and_type(146, 181, 284)
        click_and_type(147, 455, 41.2)
        click_and_type(141, 475, 87.4)
        click_and_type(135, 495, 55.1)
        click_and_type(134, 517, 6.8)
        pyautogui.press('enter')
    if keyboard.is_pressed('ctrl+alt+5'):#4-2
        click_and_type(139, 158, 1628)
        click_and_type(198, 158, -1014)
        click_and_type(146, 181, 284)
        click_and_type(147, 455, 44.7)
        click_and_type(141, 475, 87.4)
        click_and_type(135, 495, 51.6)
        click_and_type(134, 517, 6.8)
        pyautogui.press('enter')
    if keyboard.is_pressed('ctrl+alt+6'):#4-3
        click_and_type(139, 158, 1628)
        click_and_type(198, 158, -1014)
        click_and_type(146, 181, 284)
        click_and_type(147, 455, 48.2)
        click_and_type(141, 475, 87.4)
        click_and_type(135, 495, 48.4)
        click_and_type(134, 517, 6.8)
        pyautogui.press('enter')
    if keyboard.is_pressed('ctrl+alt+7'):#4-4
        click_and_type(139, 158, 1628)
        click_and_type(198, 158, -1014)
        click_and_type(146, 181, 284)
        click_and_type(147, 455, 51.6)
        click_and_type(141, 475, 87.4)
        click_and_type(135, 495, 44.9)
        click_and_type(134, 517, 6.8)
        pyautogui.press('enter')
    if keyboard.is_pressed('ctrl+alt+0'):
        break
    time.sleep(0.1)

# 按顺序执行步骤

# 