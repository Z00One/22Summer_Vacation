import random
randomValues = []

# 난수를 발생시켜 하나의 리스트에 담는다.
while len(randomValues) < 25:
    randomValue = random.randint(1,50)
    if randomValue not in randomValues:
        randomValues.append(randomValue)

# 전체 최소, 최대, 중간값
allValues = []

colList = [[], [], [], [], []]  # 행 리스트 선언
rowList = [[], [], [], [], []]  # 열 리스트 선언

# 리스트에 있는 난수를 행, 열 리스트의 5개의 리스트, 전제 값 리스트에 넣어준다.
for col in range(5):
    for row in range(5):
        colList[col].append(randomValues[0])    # 행 리스트
        rowList[row].append(randomValues[0])    # 열 리스트
        allValues.append(randomValues[0])       # 모든 값 리스트
        print("\t\t", randomValues[0], end="")
        randomValues.remove(randomValues[0])    ############### 교수님께서 다시 해보라고 말씀하신 부분
    print()

# 리스트 정렬
for index in range(5):                          ############### 교수님께서 다시 해보라고 말씀하신 부분
    colList[index].sort()   # 행 리스트 정렬
    rowList[index].sort()   # 열 리스트 정렬
allValues.sort()            # 모든 값 리스트 정렬

# 출력하기
# 열
print("열")
print("최소값", end="\t\t")
for list in rowList:
    print(list[0],end="\t\t")
print()
print("최대값",end="\t\t")
for list in rowList:
    print(list[4],end="\t\t")
print()
print("중간값",end="\t\t")
for list in rowList:
    print(list[2],end="\t\t")

# 행
print("\n")
print("행")
print("최소값", "\t\t", "최대값", "\t", "중간값")
for list in colList:
    print(" ", list[0], "\t\t", list[4], "\t\t", list[2])

# 전체
print()
print("전체")
print("최소값","\t", allValues[0])
print("최대값","\t", allValues[24])
print("중간값","\t", allValues[12])