import pyautogui

# pyautogui.mouseInfo()
pyautogui.FAILSAFE = False   # 마우스가 모니터 4 귀퉁이에 다다라도 계속 동작시킴
pyautogui.PAUSE = 1   # 모든 동작에 1초씩 sleep 적용

for i in range(10):
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)