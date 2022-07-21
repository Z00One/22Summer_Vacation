def solution(arr):
    answer = ""
    for value in arr:
        if answer[-1:] != str(value): ##### 빈리스트에는 [-1:] 로써 인덱싱 가능
            answer += str(value)
    list = []
    for value in answer:
        list.append(int(value))
    
    return list

# ########## 다른 사람 답

# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue        ### 빈리스트에는 [-1:] 로써 인덱싱 가능
#         a.append(i)
#     return a