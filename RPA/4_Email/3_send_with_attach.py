import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"
msg["From"] = EMAIL_ADDRESS   # 보내는 사람
msg["To"] = "k68424kb@naver.com"   # 받는 사람
msg.set_content("테스트 본문입니다.")   # 본문

# 파일 첨부하기(mime type)
# png 파일 첨부
with open("../2_desktop/run_btn.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)
# 엑셀 파일 첨부
with open("../1_excel/sampel_merge.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="vnd.ms-excel", filename=f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)