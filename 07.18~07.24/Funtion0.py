# 키보드로 부터 N개의 정수값 입력받아 리스트에 저장하는 함수
def inputValueList(N):
    list = []              # 입력값 담을 리스트 선언

    for index in range(N): # N개의 값 입력받기
        list.append(int(input(str(index + 1) + "번째 값을 입력하세요.")))
    
    return list

# 리스트에 저장된 정수 값을 오름차순으로 정렬하는 함수
def myBubbleSort(listValue, reverse = False):
    # 리스트의 원소를 비교
    for index in range(len(listValue) - 1):
        for compareIndex in range(len(listValue) - 1 - index):
            # 원소를 비교하여 나온 값
            compareValue = listValue[compareIndex] < listValue[compareIndex + 1] if reverse else listValue[compareIndex] > listValue[compareIndex + 1]
            
            if compareValue:    # 정렬
                if reverse:     # 내림차순
                    temp = listValue[compareIndex]
                    listValue[compareIndex] = listValue[compareIndex + 1]
                    listValue[compareIndex + 1] = temp

                else:           # 오름차순
                    temp = listValue[compareIndex + 1]
                    listValue[compareIndex + 1] = listValue[compareIndex]
                    listValue[compareIndex] = temp

    return listValue

print(myBubbleSort(inputValueList(5), reverse = True))