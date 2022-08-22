def solution(phone_book):                       # 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하는 함수 정의
    phone_book.sort()                           # 입력되는 번호를 정렬

    for index in range(len(phone_book) - 1):
        nextValue = phone_book[index + 1][:(len(phone_book[index]))] if len(phone_book[index + 1]) >= len(phone_book[index]) else "0"
        if nextValue == phone_book[index]:      # 앞의 값의 길이에 해당하는 부분이 같다면 접두어
            return False                        # 종료

    return True                                 # 해당하는 값이 없다면 접두어 없음