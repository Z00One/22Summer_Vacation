N        = 100 # 찾는 범위
FIND_NUM = 3   # 찾는 값

# 찾는 값이 있는 값 특정
for value in range(1, N + 1):
    flag = False

    if str(FIND_NUM) in str(value):
        flag = True
    
    if flag:
        print(value)