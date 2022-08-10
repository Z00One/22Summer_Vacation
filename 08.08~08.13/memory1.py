def bar(argValueA, argValueB): 
    foo(argValueB)
    argValueA = 3

def foo(argFValue):
    argFValue = 5
    han(argFValue)
    argFValue = 2
    
def han(argHValue):
    print(argHValue)

firstValue  = 1
secondValue = 2
sum = firstValue + secondValue

bar(4, sum)