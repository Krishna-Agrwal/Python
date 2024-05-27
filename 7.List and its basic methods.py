#A List is used to store multiple values irrespective of its datatype under a single variable
#List is Mutable that means, we can change individual letters of a List
#Example
l = [1,25,3,4,19,200,13.5]
print(l)

l[0] = 13
print(l)
#List is represented by : [ ]
#Example

l1 = [1,"Krishna",3,4,19, "/*", 200,13.5]
print(l1)

l2 = ["Krishna", "Manish", "Dhiraj"]
print(l2)

l4 = [1,5,8,20,1,3,6,9]
##########################################################

#Slicing of a List 
#Syntax : (Variable name[a,b-1,c])
#here, a = Starting value (Default = 0)
#b= End value 
#c = Step

print(l1[0::2])
print(l1[:1])
print(l1[:])
print(l1[0:4])

##########################################################

#Methods of String

l.append("Mohit") #To add a single element in the end of the list
print(l)
l2.append(50) #To add a single element in the end of the list
print(l2)

l[0] = 24 #To update a element of a Specific Index
print(l)

l.remove(200) #To remove a specific element fromt the list
l1.remove("Krishna") #To remove a specific element fromt the list
print(l)
print(l1)

print(l.index(13.5))  #To get the index value of a Specific element

l.extend(["krishna",20,50,"Varsha"]) #To add multiple elements in the end of the list
print(l)

l.insert(0,88) #To insert a element in a Specific Index
print(l)

l.pop(2) #To remove a specific element fromt the list using its index value
print(l) 

l1.clear() #To make the list empty
print(l1)


l4.sort() #To sort a list in either ascending or descending order
print(l4)
#Note : This method is only applicable in the list having the data of same datatype

print(l.count(10)) #To print the repition of a element in a List

print(l.reverse()) #To reverse a list
