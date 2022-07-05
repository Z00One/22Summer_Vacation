#  라인 넘버를 받아서 왼쪽에 붙는 삼각형 작성
#  라인 넘버 -> 5
# 0 *
# 1 **
# 2 ***
# 3 **
# 4 *


line_num = int(input("양의 정수 중 홀수를 입력하세요"))

# line_num = 5 일 때 중간값은 3 --> 반복은 0에서 부터 시작하기때문에 -1 을 해준다 --> 중간값은 2로 설정하고 작성
median = line_num // 2

for row_value in range(line_num):

    # 라인넘버/2 값이 세로줄이 되는 순간에 제일 많이 찍히고
    if row_value <= median :
        for col_value in range(row_value+1):
            print("*",end=" ")

    # 그 뒤로는 반대로 줄어듦
    else:
        for col_value in range(line_num - row_value):
            print("*",end=" ")

    print()
        