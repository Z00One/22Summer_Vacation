def solution(s):
    if len(s) == 4 or len(s) == 6:
        for index in range(len(s)):
            if s[index].isalpha():
                return False
        return True
    
    else:
        return False

################# 다른 사람 답
# def solution(s):
#     return s.isdigit() and len(s) in (4, 6)   조건문은 Boolean 값을 리턴 한다


# def alpha_string46(s):
#     try:                                      try, except 사용하면 오류발생 하지 않고 except를 통해 처리 가능
#         int(s)
#     except:
#         return False
#     return len(s) == 4 or len(s) == 6 