# a = " "
# if not(a.isalpha()):print(1)
# import random
# randomValues = [0 for value in range(5) ]

# # 난수를 발생시켜 하나의 리스트에 담는다.
# while len(randomValues) < 25:
#     randomValue = random.randint(1,30)
#     randomValues.append(randomValue) if randomValue not in randomValues else False

# print(randomValues)

# lowerValue = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# upperValue = [value.upper() for value in lowerValue]
# print(upperValue)

# def solution(s, n):
#     answer     = ''
#     lowerValue = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#     upperValue = [value.upper() for value in lowerValue]
    
#     for value in s:
#         if value.isupper():
#             if upperValue.index(value) + n > len(upperValue):
#                 answer += upperValue[upperValue.index(value) + n - len(upperValue)]
#             else:
#                 answer += upperValue[upperValue.index(value) + n]
        
#         elif value.islower():
#             if lowerValue.index(value) + n > len(lowerValue):
#                 answer += lowerValue[lowerValue.index(value) + n - len(lowerValue)]
#             else:
#                 answer += lowerValue[lowerValue.index(value) + n]
                
#         else:
#             answer += value
#     return answer

# print(solution("AB",1))

# s = "widhiwqds"
# s = [value for value in s]
# s.sort(reverse=True)
# print("".join(s))

# def solution(strings, n):
#     char = sorted([value[n] + value for value in strings])
#     dict = {value : value[n] + value  for value in strings}
#     answer = []
#     for charValue in char:
#         for key, value in dict.items():
#             if value == charValue:
#                 answer.append(key) 
#     return answer

# print(solution(["abce", "abcd", "cdx"], 2))

# if []: # 빈 리스트 --> Falsy
#     print(22)

def solution(arr):
    answer = ""
    for value in arr:
        if answer[-1:] != str(value): ##### 빈리스트에는 [-1:] 로써 인덱싱 가능
            answer += str(value)
    list = []
    for value in answer:
        list.append(int(value))
    
    return list
    # answer = []

    # for index1 in range(len(arr) - 1):
    #     if arr[index1] == "":
    #         continue

    #     for index2 in range(index1 + 1, len(arr)):
    #         if arr[index1] == arr[index2]:
    #             arr[index2] = ""

    #         elif arr[index1] != arr[index2] and arr[index1] != "":
    #             answer.append(arr[index1])
    #             break
    # return answer

print(solution([4,4,4,3,3]))

# print(str([4,4,4,3,3]))
# a = "11231234"
# while "11" in a:
#     a.replace("11","1")