import pyautogui

# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")   # 파일로 저장

# pyautogui.mouseInfo()
# 7,13 33,215,137 #21D789

pixel = pyautogui.pixel(7, 13)
print(pixel)

print(pyautogui.pixelMatchesColor(7, 13, (33,215,137)))   # 해당 위치(7, 13)의 RGB값을 비교해 원하는 위치에 있는지 확인