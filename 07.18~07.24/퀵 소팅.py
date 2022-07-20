def quickSort(listValue):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(listValue) <= 1:
        return listValue
    
    pivot = listValue[0]
    listValue.remove(pivot)
    
    leftSide  = [element for element in listValue if element <= pivot]
    rightSide = [element for element in listValue if element > pivot]
    
    return quickSort(leftSide) + [pivot] + quickSort(rightSide)         # 사용자 함수 a를 정의할 때 구현부분에서 a를 사용 가능
                                                                        # --> 굳이 반복문을 사용하지 않아도 반복의 개념 사용 가능
print(quickSort([2,1,5,6]))