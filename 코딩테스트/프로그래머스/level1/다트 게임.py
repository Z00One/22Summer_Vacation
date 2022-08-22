def solution(dartResult):

    pointList = []                          # 문자열 담은 변수를 담을 리스트 선언
    point     = ''                          # 문자열 담는 변수 선언

    for index in range(len(dartResult)):    # 문자열 나누기
        point   += dartResult[index]        # 문자열 담기
        nextChar = True if index == len(dartResult) - 1 else dartResult[index + 1].isdigit()

        # 0번째 인덱스가 아니고 다음인덱스의 값이 숫자인 인덱스이며 현재의 인덱스가 숫자가 아닌 경우(한 자릿수가 아닌 경우 있음)
        if index and nextChar and not(dartResult[index].isdigit()):
            pointList.append(point)         # 점수 추가
            point = ''                      # 문자열 담는 변수 초기화

    pointValues = {'S' : 1 , 'D' : 2, 'T' : 3, '*' : 2, '#' : -1}

    for index in range(len(pointList)):     # 각각의 점수들 숫자로 교체
        pointNum = 0                        # 숫자로 교채한 점수 담아줄 변수 선언
        point = ''                          # 숫자인 문자를 담아줄 변수 선언

        for value in pointList[index]:      # 각각의 문자들 숫자로 교체
            if value.isdigit():             # 숫자일 경우
                point += value

            else:                           # 숫자가 아닌 경우
                if value.isalpha():         # 문자일 경우
                    pointNum += int(point)  # 숫자 더해주기

                pointNum = pointNum * pointValues[value] if value == '*' or value == '#' else pointNum ** pointValues[value]
                
                if index and value == '*':  # *은 이전 점수에도 영향 있음
                    pointList[index - 1] *= pointValues[value]

        pointList[index] = pointNum         # 점수를 숫자로 교체
    sum = 0                                 # 점수의 합계를 담을 변수 선언

    for value in pointList:                 # 점수 담기
        sum += value

    return sum                              # 합계 반환

print(solution('1D2S#10S'))