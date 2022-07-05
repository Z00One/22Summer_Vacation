#  라인 넘버를 받아서 왼쪽에 붙는 삼각형 작성
#  라인 넘버 -> 5
# 1 *
# 2 **
# 3 ***
# 4 **
# 5 *

line_num = int(input("양의 정수 중 홀수 하나를 입력하세요"))

median = line_num // 2 + 1
row_count = 1
while row_count <= line_num:
    col_count = 1
    # 세로 값이 중간값보다 작을 경우
    if row_count <= median:
        while col_count <= row_count:
            print("*", end=" ")
            col_count+=1
    # 세로 값이 중간값보다 클 경우
    else :
        while col_count <= line_num - row_count + 1: # col_value 값이 전체 라인넘버에서 세로 값을 빼고 1을 더해준 값보다 작을 때만 반복
            print("*", end=" ")
            col_count+=1
    print()
    row_count+=1