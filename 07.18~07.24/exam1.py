N   = 5 # 반복횟수
sum = 0 # 합계

# 입력값 합계에 담기
for index in range(N):
    sum += int(input(str(index+1) + "번째 값 입력"))

avg = sum / N # 평균

print("합계 :", sum)
print("평균 :", avg)