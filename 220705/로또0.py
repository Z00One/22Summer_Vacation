import random as ran
# 1 ~ 45 중복되지 않는 로또 번호
# 번호를 리스트에 담아준다.
num_list = [num for num in range(1,46)] # [1, 2, 3, 4 ... 45]
# 
len_count = 44 # 인덱스는 0부터 시작
lotto_num_list = []

# 6개 뽑기 -> for
for num in range(6):
    # num_list에서 한 인덱스를 뽑는다.
    lotto_num = num_list[ran.randint(1,len_count)]
    # lotto_num 값이 중복되지 않도록 해당 인덱스를 제거
    num_list.remove(lotto_num)
    # lotto_num_list에 lotto_num을 append
    lotto_num_list.append(lotto_num)
    # lotto_num 값이 중복되지 않도록 lotto_num_list의 길이 줄여준다.
    len_count-=1
print(lotto_num_list)