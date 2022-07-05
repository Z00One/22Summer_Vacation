# * 5x5 세 번 출력
# 가로, 세로, 메트릭스 값 선언
col = 5
row = 5
matrix = 3

# 메트릭스를 카운트할 변수 선언
matrix_count = 1

# Matrix의 범위
while matrix_count <= matrix:

    # matrix_count값이 바뀌면 세로 카운트 리셋
    row_count = 1

    # 세로 반복
    while row_count <= row:
        
        # 세로가 바뀌면 가로카운트 리셋
        col_count = 1

        # 가로 반복
        while col_count <= col:
            print("*", end="")

            # 가로 값 카운트
            col_count += 1

        # 세로 바꾸기
        print()

        # 반복이 끝나면 세로 값 카운트
        row_count += 1

    # 매트릭스 바꾸기
    print()
    # 반복이 끝나면 매트릭스 값 카운트
    matrix_count += 1
