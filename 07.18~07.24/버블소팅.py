def bubbleSort(listValue):                                  # 버블 소팅 오름차순 정렬
    for index in range(len(listValue)-1):
        for nextIndex in range(index + 1, len(listValue)):  # 앞의 값이 뒤의 값 보다 클 경우 자리를 바꿔준다.
            if listValue[index] > listValue[nextIndex]:
                temp = listValue[index]
                listValue[index] = listValue[nextIndex]
                listValue[nextIndex] = temp
    return listValue

print(bubbleSort([5,4,2,2,1,5,6]))