from imap_tools import MailBox
from account import *


with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=5, reverse=True):   # 5개 최근 메일 다 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(UNSEEN)'):   # 읽지 않은 메일 가져오기
    #       print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(FROM ksw1238@gmail.com)', limit=3, reverse=Ture):   # 특정인이 보낸 메일 가져오기
    #       print("[{}] {}".format(msg.from_, msg.subject))

    # 작은 따옴표로 먼저 감싸고, 실제 TEXT 부분은 큰 따옴표로 감싸주세요
    # for msg in mailbox.fetch('(TEXT "test mail")'):   # 'test' 'mail'이라는 각각의 단어를 포함하는 메일을 search(제목, 본문)
    #       print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SUBJECT "test mail")'):   # 'test' 'mail'이라는 각각의 단어를 포함하는 메일을 search(제목만) , 한글X
    #       print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch(limit=5, reverse=True):   # 어떤 글자(한글)을 포함하는 메일 필터링(제목만)
    #       if "테스트" in msg.subject:
    #           print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SENTSINCE 07-Dec-2020)'):   # 특정 날짜 이후의 메일 가져오기
    #       print("[{}] {}".format(msg.from_, msg.subject))
    
    # for msg in mailbox.fetch('(ON 12-Dec-2020)'):   # 특정 날짜에 온 메일
    #       print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(ON 12-Dec-2020 SUBJECT "Robert")', reverse=True):   # 2가지 이상의 조건을 모두 만족하는 메일
    #       print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailbox.fetch('(OR ON 12-Dec-2020 SUBJECT "test")', reverse=True):   # 2가지 이상의 조건중 하나라도 만족하는 메일
          print("[{}] {}".format(msg.from_, msg.subject))