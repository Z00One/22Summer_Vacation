import random as ran
# 1 ~ 45 중복되지 않는 로또 번호
# 로또 번호를 리스트에 담아준다.
num_list = [num for num in range(1,46)]
len_count = 45
lotto_num = []
# 6개 뽑기 -> for
for num in range(6):
    lotto_num.append(num_list[ran.randint(0,len_count-1)])
    # 중복되지 않도록
    len_count-=1
print(lotto_num)