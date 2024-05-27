#Taking a String Input
a = input("Enter Data:")
print(a)

#Taking a Integer Input
#Method 1
b = int(input("Enter Data:"))
print(b)
#Method 2
c = input("Enter Data: ")
print(int(c))

#Taking a input of any Datatype
d = eval(input("Enter Data:"))
print(d)

#Taking Multiple inputs in a single line
e,f = input("Enter Data: ").split()
print(e)
print(f)
print(e,f)