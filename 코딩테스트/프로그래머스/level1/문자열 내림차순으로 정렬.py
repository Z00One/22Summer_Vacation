def solution(s):
    s = [value for value in s]
    s.sort(reverse=True)
    return "".join(s)

################# 다른 사람 답

# def solution(s):                              # list.sort() 는 기존의 값을 정렬           --> 문자열 사용 불가능
#     return ''.join(sorted(s, reverse=True))   # newList = sorted(list) 는 정렬한 값을 반환

