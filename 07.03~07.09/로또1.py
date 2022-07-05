# random 모듈 import
import random as r
# 당첨 번호를 담을 lotto_num, 당첨번호를 추가한 횟수를 담을 num_count 선언
lotto_num = []
num_count = 0

while num_count <6 :
    # 번호 뽑기
    num = r.randint(1,45)
    # 번호가 lotto_num 안에 없다면 추가 해주기
    if num not in lotto_num:
        lotto_num.append(num)
        # 번호 추가한 횟수 카운트
        num_count += 1

print(lotto_num)
