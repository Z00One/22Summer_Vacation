last_value = int(input("수를 입력해요"))
list1 = [value for value in range(1,last_value+1)] # [1, 2, 3, 4, ... last_value]

list2 = []
index = 0
while len(list2) < len(list1):
    list.append(list1[index]) # 오류남
    print(list2[0:])
    index += 1