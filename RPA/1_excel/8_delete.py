from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.delete_rows(7)   # 7번째 줄에 있는 6번 학생 데이터 삭제
# ws.delete_rows(8, 3)   # 8번째 줄부터 3줄을 삭제
#
# wb.save("sample_delete_row.xlsx")

# ws.delete_cols(2)   # 2번째 열 (B) 삭제
ws.delete_cols(2, 2)   # 2번째 열부터 2개 열 삭제
wb.save("sample_delete_col.xlsx")