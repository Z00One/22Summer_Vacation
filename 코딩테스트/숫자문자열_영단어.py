def solution(s):
    # 숫자에 해당하는 영단어가 있다 --> dictionary
    dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9' }
    # 입력된 문자열을 하나씩 카운트한다
    alpha_count = ""
    for value in s:
        # 문자일 경우에만 카운트한다
        if value.isalpha():
            alpha_count+=value
        # 카운트하는 도중에 영단어가 완성이 된다면 해당하는 숫자로 바꿔준다.
        if alpha_count in dict.keys():
            s=s.replace(alpha_count,dict[alpha_count])
            alpha_count = ""
    return int(s)
