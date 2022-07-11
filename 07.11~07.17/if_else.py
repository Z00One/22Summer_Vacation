cat = 'cat'
dog = 'dog'
ret = None

# 2. if - eles 문 #
animal = 'cat'
# if animal is dog:
#     ret = dog
# else:
#     ret = cat
# print("Default: " + ret)

ret = dog if animal is dog else cat # animal = dog 면 ret = dog, 아니면 ret = cat 
print("One-Line: " + ret)
