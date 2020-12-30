import pyautogui

# fw = pyautogui.getActiveWindow()   # 현재 활성화된 창
# print(fw.title)   # 창의 제목 정보
# print(fw.size)   # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.bottom)   # 창의 좌표 정보
# pyautogui.click(fw.left + 25, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w)   # 모든 윈도우 가져오기

w = pyautogui.getWindowsWithTitle("제목 없음")[0]   # 메모장이나 그림판에 아무것도 저장하지 않은 상태로 띄워놓고 테스트
print(w)
if not w.isActive:   # 현재 활성화가 되어있지 않다면
    w.activate()   # 활성화 ( 맨 앞으로 가져오기)

if not w.isMaximized:   # 현재 최대화가 되지 않았다면
    w.maximize()   # 최대화

# if w.isMinimized == False:   # 현재 최소화가 되지 않았다면
#     w.minimize()   # 최소화
pyautogui.sleep(1)
w.restore()   # 화면 원복

w.close()   # 윈도우 닫기

