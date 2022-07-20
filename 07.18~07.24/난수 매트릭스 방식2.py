def bubbleSort(listValue):                                  # 버블 소팅 오름차순 정렬
    for index in range(len(listValue)-1):                   # index == len(listValue) 일 때는 이미 소팅이 끝나 비교를 할 수 없는 상황
        for nextIndex in range(index + 1, len(listValue)):  # set된 index의 원소와 뒤에 nextIndex의 원소를 비교한다. 
            if listValue[index] > listValue[nextIndex]:     # index의 원소가 더 크다면 자리를 바꿔준다.
                temp = listValue[index]
                listValue[index] = listValue[nextIndex]
                listValue[nextIndex] = temp
    return listValue

import random
randomValueList = []

# 난수를 발생시켜 하나의 리스트에 담는다.
while len(randomValueList) < 25:
    randomValue = random.randint(1,50)
    if randomValue not in randomValueList:
        randomValueList.append(randomValue)

colList = [[], [], [], [], []]  # 행 리스트 선언
rowList = [[], [], [], [], []]  # 열 리스트 선언

# 리스트에 있는 난수를 행, 열 리스트의 5개의 리스트, 전제 값 리스트에 넣어준다.
for col in range(5):
    for row in range(5):
        colList[col].append(randomValueList[col * 5 + row])    # 행 리스트
        rowList[row].append(randomValueList[col * 5 + row])    # 열 리스트
        print("\t\t", randomValueList[col * 5 + row], end="")
    print()

# 리스트 정렬
for index in range(5):                          ############### 교수님께서 다시 해보라고 말씀하신 부분
    bubbleSort(colList[index])   # 행 리스트 정렬
    bubbleSort(rowList[index])   # 열 리스트 정bubbleSort(colList)         
bubbleSort(randomValueList)      # 난수 리스트 정렬

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
print("\n\n행")
print("최소값", "\t\t", "최대값", "\t", "중간값")
for list in colList:
    print(" ", list[0], "\t\t", list[4], "\t\t", list[2])

# 전체
print()
print("전체")
print("최소값","\t", randomValueList[0])
print("최대값","\t", randomValueList[24])
print("중간값","\t", randomValueList[12])