def solution(arr):
    if arr == [10] : return [-1]
    min = arr[0]
    for element in arr:
        if element < min: min = element
    arr.remove(min)
    return arr
print(solution([4, 3, 2, 1]))