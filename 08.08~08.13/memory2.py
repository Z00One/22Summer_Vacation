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
    
    return f_temp # bar에 남아있을 수 있다.(-> 언어에따라 다름) 변수와 달리 이름이 없어서 값을 가져오진 못한다.
    
def han(argHA):
    print(argHA)

myList =[2, 3]

bar(myList)

print(myList)