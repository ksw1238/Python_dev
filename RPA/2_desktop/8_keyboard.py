import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]   # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("나도코딩")   # 한글은 입력이 안됨

# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 1번 l a 적고 엔터버튼
# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)

# print(pyautogui.KEYBOARD_KEYS)   # 사용 가능한 키보드 정보

# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift")   # shift 키를 누른 상태에서
# pyautogui.press("4")   # 숫자 4를 입력하고
# pyautogui.keyUp("shift")   # shift 키를 땐다

# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")   # Ctrl 누르고 Alt 누르고 Shift 누르고 A 누르고 A 떼고 Shift 때고 alt 때고 Ctrl 때고
# pyautogui.hotkey("ctrl", "a")

import  pyperclip
# pyperclip.copy("나도코딩")   # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v")   # 클립보드에 있는 내용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    
my_write("나도 코딩")

# win : ctrl + alt + del --> 자동화 프로그램 종료