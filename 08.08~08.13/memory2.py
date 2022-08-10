def bar(argA):
    b_temp = 1
    argA.append(b_temp)
    foo(argA)
    argA.append(True)
    
def foo(argFA):
    del argFA[0]
    f_temp = "hello"
    han(f_temp)
    f_temp = "jung"
    
    return f_temp
    
def han(argHA):
    print(argHA)

myList =[2, 3]

bar(myList)

print(myList)