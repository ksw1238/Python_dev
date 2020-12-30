import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"
msg["From"] = EMAIL_ADDRESS   # 보내는 사람
# msg["To"] = "k68424kb@naver.com"   # 받는 사람

# 여러 명에게 메일을 보낼 때
to_list = ["k68424kb@naver.com", "ksw1238@hanmail.net"]
msg["To"] = ", ".join(to_list)

# 참조
# msg["Cc"] = "ksw1238@gmail.com"

# 비밀참조
# msg["Bcc"] = "ksw1238@gmail.com"

msg.set_content("테스트 본문입니다.")   # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)