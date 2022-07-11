dict = {}
list = [1,2,3,4,5,1,2,3,4,5]
for key in list:
    if key not in dict:
        dict[key] = 1
    else :
        dict[key] += 1
for key, value in dict.items():
    if value>=2:
        print(key, value)