# 가로 세로 값 선언
col = 5
row = 5
# 두 개의 매트릭스
for matrix_value in range(2):

    # col 값 만큼 세로 반복
    for row_value in range(row):

        # row 값 만큼 가로 반복
        for col_value in range(col):

            # 첫 번째 매트릭스
            if matrix_value == 0:

                # (세로값이 홀수 이면서 세로값과 가로값이 같을 때) or (세로값이 홀수 이면서 가로 값이 전체 가로값에서 높이값을 빼고 1을 더한 값과 같을 때)
                if (row_value % 2 == 1 and col_value == row_value) or (row_value == row_value % 2 == 1 and row - 1 - col_value):
                    # 공백 출력
                    print(" ", end='')

                # 그 이외의 경우 별을 출력
                else:
                    print("*", end="")

            # 두 번째 매트릭스
            else:
                # 가로 값과 세로 값이 같을 때는 공백 출력
                if col_value == row_value:
                    print(" ", end='')

                # 그 이외의 경우 별을 출력
                else:
                    print("*", end="")
                    
        # 세로 바꿔주기
        print()

    # 메트릭스 구분하기
    print()
