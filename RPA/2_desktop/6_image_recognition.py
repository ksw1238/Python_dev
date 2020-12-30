import pyautogui
import time
import sys

# pyautogui.mouseInfo()

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")   # 그림파일과 동일한 화면을 찾음
# pyautogui.moveTo(trash_icon)   # 해당 위치로 커서 이동

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)   # 그림파일과 동일한 화면을 찾지 못하면 'None'을 반환

# 속도 개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1500, 60, 100, 200))
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.7)   # 70% 정확도 체크
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")

# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#
# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기(TimeOut)
# timeout = 10   # 10초 대기
# start = time.time()   # 시작 시간 설정
# file_menu_notepad = None
#
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()   # 종료 시간 설정
#     if end - start > timeout:   # 지정한 시간이 10초를 초과하면
#         print("시간 종료")
#         sys.exit()

# pyautogui.click(file_menu_notepad)


def find_tartget(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_tartget(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 10)