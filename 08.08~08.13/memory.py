def bar(argA):
    argA = argA + 1
    foo(argA)
    
def foo(argB):
    print(argB)
    
value = 1

bar(value)

print(value)