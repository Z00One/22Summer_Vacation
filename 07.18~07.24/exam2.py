while True:
    value = int(input("정수를 입력하세요"))
    # 입력값 구분
    if value > 0:
        print("양수입니다.")

    elif value < 0:
        print("음수입니다.")
        
    else:
        break