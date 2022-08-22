def solution(a, b):
    dayOfTheWeek    = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]     # 1월 1일은 금요일 1 % 7 = 1 -> 1을 인덱스 값으로 사용
    
    dayOfMonth      = {2 : 31, 3 : 29, 4 : 31, 5 : 30, 6 : 31, 7 : 30, 8 : 31, 9 : 31, 10 : 30, 11 : 31, 12 : 30}       # 달 마다 지난 달의 일수
    
    day = 0
                                        # 총 일수 구하기
    if a != 1:                          # 한 달이라도 지난 경우
        for month in range(2, a + 1):
            day += dayOfMonth[month]
        day += b
    else:                               # 1월인 경우
        day += b
    
    day %= 7                            # 요일 구하기
    
    return dayOfTheWeek[day]            # 요일 반환

print(solution(11, 1))