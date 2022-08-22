def solution(survey, choices):
    compareValue = {'RT' : {'R' : 0 , 'T' : 0}, 'CF' : {'C' : 0, 'F' : 0}, 'JM' : {'J' : 0, 'M' : 0}, 'AN' : {'A' : 0 , 'N' : 0}}

    for index in range(len(survey)):                                    # 값 분류
        key = "".join(sorted(survey[index]))

        if choices[index] < 4:
            compareValue[key][survey[index][0]] += 4 - choices[index]

        elif choices[index] > 4:
            compareValue[key][survey[index][1]] += choices[index] - 4

    answer = ''                                                         # 분류한 값에 따라 성격유형을 담아줄 변수 선언

    for key in compareValue.keys():                                     # 출력값 특정
        if compareValue[key][key[0]] >= compareValue[key][key[1]]:      # 우세한 성격유형 특정
            alpha = key[0]

        else:
            alpha = key[1]

        answer += alpha

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))