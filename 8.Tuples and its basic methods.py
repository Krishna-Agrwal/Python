#A Tuple is also used to store multiple values irrespective of its datatype under a single variable
#Tuple is immutable that means, we can't change individual letters of a string
#Example
t = (1,25,3,4,19,200,13.5)
print(t)

t[0] = 18
print(t) #It will given an error, becuase editing a tuple is not possible
#Tuple is represented by : ( )


#Example
t = (1,25,3,4,19,200,13.5)
print(t)

t1 = (1,"Krishna",3,4,19, "/*", 200,13.5)
print(t1)

t2 = ("Krishna", "Manish", "Dhiraj")
print(t2)

##########################################################

#Slicing of Tuple 
#Syntax : (Variable name[a,b-1,])
#here, a = Starting value (Default = 0)
#b= End value 

print(t1[0::])
print(t1[:1])
print(t1[:])
print(t1[0:4])

##########################################################

#Some Methods of Tuple

print(len(t)) #To find the length of the tuple
print(t.count(1)) #To count the repition of an element
print(t.index(200)) #To get the index of a element present in the tuple
print(max(t)) #To get the maximum value from the tuple
print(min(t)) #To get the minimum value from the tuple