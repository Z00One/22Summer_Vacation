mystring = "#heelo!"

mylist = [element for element in mystring if element.islower() or element != "#"]

print(mylist)