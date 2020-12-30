from tkinter import *
from DATA import *   # DATA.py 파일

root = Tk()
root.title("데이터 변경 모니터링")
root.geometry("400x480") # 가로 * 세로

# DATA.py의 SAP 펑션 콜
def Execute_SAP():
    Monitoring_SAP(txt_ID.get(), txt_PW.get())


# JOYBILL & HR 프레임
WEB_frame = LabelFrame(root, text="JOYBILL & HR Monitoring")
WEB_frame.pack(fill="x", padx=10, pady=10)

# 원본 경로 표시
path_src_frame = LabelFrame(WEB_frame, text="원본경로")
path_src_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_src_path = Text(path_src_frame, width=50, height=4)
txt_src_path.pack()
txt_src_path.insert(END, source_path)
txt_src_path.configure(background="gray92", state="disabled")

# 저장 경로 표시
path_dest_frame = LabelFrame(WEB_frame, text="저장경로")
path_dest_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Text(path_dest_frame, width=50, height=4)
txt_dest_path.pack()
txt_dest_path.insert(END, target_path)
txt_dest_path.configure(background="gray92", state="disabled")

# 실행 버튼 (JOYBILL & HR)
frame_WEB_btn = Frame(WEB_frame)
frame_WEB_btn.pack(fill="x", padx=10, pady=5)  # 간격 띄우기

btn_JOYBILL = Button(frame_WEB_btn, padx=5, pady=5, width=12, text="JOYBILL", command=Monitoring_JOYBILL)   # 조이빌
btn_JOYBILL.pack(side="left", padx=10, pady=5)

btn_HR = Button(frame_WEB_btn, padx=5, pady=5, width=12, text="HR", command=Monitoring_HR)   # HE
btn_HR.pack(side="right", padx=10, pady=5)



### SAP 모니터링 Frame ###
SAP_frame = LabelFrame(root, text="SAP Monitoring")
SAP_frame.pack(fill="x", padx=10, pady=20)

# ID & PW
frame_ID = Frame(SAP_frame)
frame_ID.pack(fill="x", padx=10, pady=1)

txt_ID = Entry(frame_ID)
txt_ID.pack(side="right", padx=3, pady=5, ipadx=13, ipady=3)  # ID 입력
txt_ID.insert(END, "IT00")

lbl_ID = Label(frame_ID, text="ID", width=3)
lbl_ID.pack(side="right", padx=1, pady=5)

frame_PW = Frame(SAP_frame)
frame_PW.pack(fill="x", padx=10, pady=1)

txt_PW = Entry(frame_PW, show="*")
txt_PW.pack(side="right", padx=3, pady=5, ipadx=13, ipady=3)  # PW 입력

lbl_PW = Label(frame_PW, text="PW(ID & 사번)", width=12)
lbl_PW.pack(side="right", padx=1, pady=5)

# 실행 버튼 (SAP)
frame_SAP_btn = Frame(SAP_frame)
frame_SAP_btn.pack(fill="x", padx=10, pady=5)

btn_SAP = Button(frame_SAP_btn, padx=5, pady=5, width=12, text="SAP", command=Execute_SAP)
btn_SAP.pack(side="right", padx=10, pady=5)

root.resizable(False, False)
root.mainloop()