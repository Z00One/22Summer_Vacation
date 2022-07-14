# cat = 'cat'
# dog = 'dog'
# ret = None

# # 2. if - eles 문 #
# animal = 'cat'
# # if animal is dog:
# #     ret = dog
# # else:
# #     ret = cat
# # print("Default: " + ret)

# ret = dog if animal is dog else cat # animal = dog 면 ret = dog, 아니면 ret = cat 
# print("One-Line: " + ret)

# a = 16

# a %= 10

# print(a)

# count = 0
# list  =  ["heello", "hello world", "   hello whoe hello"]
# for value in list:
#     if "hello" in value:
#         count += 1
# print(count)

# a = "sdsfg"

# # s = a / "s"

# # print(s)

# list = [input("  ")]

# print(list)
# # 몇 회 입력받을지 정하기
# rangeValue  = int(input("입력 문자열의 줄(Line) 수를 입력하세요!"))
# inputString      = []                                                 # 입력 받은 문자열을 저장할 리스트
# line = []
# searchValue = 0
# for index in range(rangeValue):
#     inputString.append([])
#     inputValue = input("%d 번째 라인의 문자열을 입력하세요."%(index+1))
#     #  영문 문자열을 키보드로부터 입력 받아 List에 저장 후,
#     for value in inputValue:
#         inputString[index].append(value)
# print(inputString)

a = " "
if a.isdigit():
    print("true")
else : 
    print("false")


# a = ["SS","asad","hello"]
# if "hello" in a:
#     print ("hel")