# a = " "
# if not(a.isalpha()):print(1)
import random
randomValues = [0 for value in range(5) ]

# 난수를 발생시켜 하나의 리스트에 담는다.
while len(randomValues) < 25:
    randomValue = random.randint(1,30)
    randomValues.append(randomValue) if randomValue not in randomValues else False

print(randomValues)