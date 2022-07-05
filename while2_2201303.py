# 가로 값 세로 값 메트릭스 값 선언
col = 5
row = 5
matrix = 2

# 매트릭스 카운트 할 변수 선언
matrix_count = 0

# 매트릭스 돌리기
while matrix_count < matrix:

    # 매트릭스 돌릴 때 마다 row_count 값 리셋
    row_count = 1

    # 세로 돌리기
    while row_count <= row:

        # 세로 돌릴 때 마다 col_count 값 리셋
        col_count = 1
        
        # 가로 찍어주기
        while col_count <= col:

            # 매트릭스가 0인 경우
            if matrix_count == 0:
                # (세로값이 짝수 이면서 세로값과 가로값이 같을 때) or (세로값이 짝수 이면서 가로 값이 전체 가로값에서 높이값을 빼고 1을 더한 값과 같을 때)
                if (row_count % 2 == 0 and col_count == row_count) or (row_count % 2 == 0 and col_count == col - row_count + 1):
                    # 공백 처리
                    print(" ", end='')
                # 그 이외에는 별 처리
                else:
                    print("*", end='')
        # 매트릭스가 0인 경우 이외 (이 코드에선 1인 경우)
            else:
                # 세로 값과 홀수 값이 같은 경우 공백 처리
                if row_count == col_count:
                    print(" ", end='')
                # 그 이외에는 별 처리
                else:
                    print("*", end='')
                
            # 반복이 끝나면 가로 값 카운트
            col_count += 1

        # 반복이 끝나면 세로 값 카운트
        row_count += 1

        # 세로 끝나면 줄 바꿔주기
        print()

    # 메트릭스 끝나면 줄 바꿔주기
    print()

    # 반복이 끝나면 매트릭스 값 카운트
    matrix_count += 1