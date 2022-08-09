# 키보드로 부터 N개의 정수값 입력받아 리스트에 저장하는 함수
def inputValueList(N):
    list = []                                                                       # 입력값 담을 리스트 선언

    for index in range(N):                                                          # N개의 값 입력받기
        list.append(int(input(str(index + 1) + "번째 값을 입력하세요.")))
    
    return list

# 리스트에 저장된 정수 값을 오름차순으로 정렬하는 함수
def myBubbleSort(listValue, reverse = False):
    
    for index in range(len(listValue) - 1):                                         # 리스트의 원소를 비교
        for compareIndex in range(len(listValue) - 1 - index):
            
            compareValue = listValue[compareIndex] > listValue[compareIndex + 1]    # 원소를 비교하여 나온 Boolean 값

            # 정렬
            if compareValue:                                                        # 오름차순
                temp = listValue[compareIndex + 1]  
                listValue[compareIndex + 1] = listValue[compareIndex]
                listValue[compareIndex] = temp

                                                                                    # 내림차순
    listValue = [listValue[index] for index in range(len(listValue)-1 , -1, -1)] if reverse else listValue
    
    return listValue
   
print(myBubbleSort(inputValueList(5)))