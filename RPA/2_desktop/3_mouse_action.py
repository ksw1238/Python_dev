import pyautogui

# pyautogui.sleep(3)   # 3초 대기
# print(pyautogui.position())

# pyautogui.click(41, 18, duration=1)   # 1초 동안 (41, 18) 좌표로 이동 후 마우스 클릭

# pyautogui.doubleClick()   # 더블클릭
# pyautogui.click(clicks=500)   # 500번 클릭

# 마우스 drag & drop
# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()
# pyautogui.moveTo(1000, 500, duration=2)
# pyautogui.mouseUp()

# pyautogui.drag(100, 0, duration=0.25)   # 현재 위치 기준으로 100, 0 만큼 드레그
# pyautogui.dragTo(1000, 300, duration=0.25)   # 절대좌표 기준으로 1000, 300 으로 드레그


pyautogui.sleep(3)
# pyautogui.rightClick()   # 마우스 오른쪽 클릭
# pyautogui.middleClick()   # 마우스 휠 클릭

pyautogui.scroll(-300)   # 아래 방향으로 300만큼 스크롤
pyautogui.scroll(300)   # 위 방향으로 300만큼 스크롤
