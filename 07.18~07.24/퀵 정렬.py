list = [5,4,8,4,9,1,6,2,7]

# pivot값 설정
pivot = list[0]
list2 = []
list3 = []
for index in range(len(list)):    
    # pivot보다 큰 경우 pivot 오른쪽으로 
    value = list[index]
    if list[index] > pivot:
        # list.remove(list[index])
        # list.insert(list.index(pivot) + 1,value)
        list2.append(value)
    # pivot보다 작은 경우 pivot 왼쪽으로
    if list[index] < pivot:
        # list.remove(list[index])
        # list.insert(list.index(pivot),value)
        list3.append(value)

list.append(pivot)

pivot2 = list2[0]
pivot3 = list3[0]

for index in range(len(list2)):    
    # pivot보다 큰 경우 pivot 오른쪽으로 
    value = list2[index]
    if list2[index] > pivot:
        list2.remove(list2[index])
        # list.insert(list.index(pivot) + 1,value)
        list2.append(value)
    # pivot보다 작은 경우 pivot 왼쪽으로
    if list2[index] < pivot:
        list2.remove(list2[index])
        list.insert(list.index(pivot2),value)
        # list2.append(value)
print(list2)