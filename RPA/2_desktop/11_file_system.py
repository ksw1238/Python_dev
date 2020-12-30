# 파일 기본
import os

# print(os.getcwd())   # current working directory 현재 작업 공간
# os.chdir("C:/Users/james/Desktop/Python_dev/RPA")   # rpa_basic 으로 작업 공간 이동
# print(os.getcwd())
# os.chdir("..")   # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..")   # 조부모 폴더로 이동
# print(os.getcwd())

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt")   # 절대 경로 생성
# print(file_path)

# 파일이 위치한 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\james\Desktop\Python_dev\RPA\my_file.txt"))

# 파일 정보 가져오기
import time
import datetime

# 파일의 생성 날짜
# filepath = "run_btn.png"
# ctime = os.path.getctime(filepath)
# print(ctime)
# # 날짜 정보를 strftime을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))
#
# # 파일의 수정 날짜
# mtime = os.path.getmtime(filepath)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))
#
# # 파일의 마지막 접근 날짜
# atime = os.path.getatime(filepath)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))
#
# # 파일 크기
# size = os.path.getsize(filepath)
# print(size)   # 바이트 단위로 파일 사이즈 가져오기

# 파일 목록 가져오기
# file_list = os.listdir()   # 모든 폴더, 파일 목록 가져오기
# file_list = os.listdir("..")   # 상위 폴더의 모든 폴더, 파일 목록 가져오기
# print(file_list)

# 파일 목록 가져오기 (하위 폴더 모두 포함)
# result = os.walk("..")   # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
# print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)

# 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk(os.getcwd()):
#     if name in files:
#         result.append(os.path.join(root, name))
# print(result)

# 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, *.txt, 자동화*.png
# import fnmatch
# pattern = "*.xlsx"   # .xlsx로 끝나는 모든 파일
# result = []
# for root, dirs, files, in os.walk(".."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):   # 이름이 패턴과 일치하면
#             result.append(os.path.join(root, name))
# print(result)

# # 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir(".."))   # 폴더인지? True
# print(os.path.isfile(".."))   # 파일인지? False
#
# print(os.path.isdir("run_btn.png"))
# print(os.path.isfile("run_btn.png"))
#
# # 만약에 지정된 경로에 해당하는 파일/폴더가 없다면?
# print(os.path.isdir("run_btnn.png"))   # 없으면 False
#
# # 주어진 경로가 존재하는지?
# if os.path.exists(".."):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")
    
# 파일 만들기
# open("new_file.txt", "a").close()   # 빈 파일 생성

# 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt")   # new_file_rename.txt로 파일명 변경

# 파일 삭제하기
# os.remove("new_file_rename.txt")

# 폴더 만들기
# os.mkdir("new_folder")
# os.makedirs("new_folder/a/b/c")   # 하위 폴더를 가지는 폴더 생성

# 폴더명 변경하기
# os.rename("new_folder", "new_folder_rename")

# 폴더 삭제하기
# os.rmdir("new_folder")
# os.removedirs("new_folder/a/b/c")

import shutil
# 모든 파일이 삭제될 수 있으므로 주의!!
# shutil.rmtree("new_folders")   # 폴더 안이 비어있지 않아도 완전 삭제 가능

# 파일 복사하기
# 어떤 파일을 안으로 복사하기
# shutil.copy("run_btn.png", "../../test_folder")   # 원본 경로, 대상 경로
# shutil.copy("run_btn.png", "../../test_folder/copied_run_btn.png")   # 원본경로, 대상경로(파일명 변경)
# shutil.copyfile("run_btn.png", "../../test_folder/copied_run_btn2.png")   # 원본경로, 대상경로와 파일명(파일명 변경)
# shutil.copy2("run_btn.png", "../../test_folder/copy2.png")   # 원본경로, 대상경로와 파일명(파일명 변경)
# copy, copyfile : 메타정보 복사 X
# copy2          : 메타정보 복사 O

# 폴더 복사
# shutil.copytree("../../test_folder", "../../test_folder2")   # 원본폴더 경로, 대상폴더 경로

# 폴더 이동
# shutil.move("../../test_folder", "test_folder3")
shutil.move("test_folder3", "../../test_folder")   # 폴더를 이동시키면서 폴더명 변경