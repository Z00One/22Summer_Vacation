ROW = 5 # 세로 값
COL = 5 # 가로 값

# 2차원 돌리기 rowValue값 만큼 공백 출력, COL - rowValue 만큼 * 출력
for rowValue in range(ROW):
    print(" " * rowValue, end="")

    for colValue in range(COL - rowValue):
        print("*",end="")

    print()