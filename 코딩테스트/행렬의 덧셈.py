def solution(arr1, arr2):
    
    for element in range(len(arr1)): # 더해줄 요소 정하기
        for index in range(len(arr1[element])): # 더해줄 요소의 인덱스 정하기
            arr1[element][index] += arr2[element][index]
            
    return arr1

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))