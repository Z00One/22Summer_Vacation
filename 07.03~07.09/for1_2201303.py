# 가로 값 세로 값 선언
col = 5
row = 5

# matrix 세 번 반복
for matrix in range(3):

    # row값 만큼 세로 반복
    for row_value in range(row):
        
        # col값 만큼 가로 반복
        for col_value in range(col):
            print("*", end="")

        # 단 바꾸기
        print()

    # 메트릭스 구분하기
    print()
