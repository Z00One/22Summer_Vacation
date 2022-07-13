def solution(s):
    # # p와 y의 갯수 알아보기
    p_count = 0
    y_count = 0
    # 반복 사용해서 알아보기
    for char in s:
        if char == "P" or char == "p":
            p_count += 1
        if char == "Y" or char == "y":
            y_count += 1
    # 개수가 같다면
    if p_count == y_count:
        return True
    else: return False

    # 문자열에서 p,y가 아닌 값들만 카운트해서 그 길이를 나눴을 때 짝수면 True, 홀수면 False
    # 소문자로 통일
    # p,y만 추출
    # py_count = 0
    # s = s.lower()
    # for value in s:
    #     if value == "p" or value == "y":
    #         py_count += 1
    # if py_count % 2 == 0: return True
    # else: return False
    # 길이를 나눠보기
    # s = s.lower()
    # p랑 y가 아닌 경우

    # new = ["p","y","P","Y"]
    # answer = [ele for ele in s if ele in new]
    # if len(answer) % 2 == 1:
    #     return False
    # else:
    #     return True    # 

    # p 나 y 가 아닌 경우를 빼주기
    new = ["p","y","P","Y"]
    answer = [ele for ele in s if ele in new]
    if len(answer) % 2 == 1:
        return False
    else:
        return True
print(solution("ssssssssssssssssPyy"))
