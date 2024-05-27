#A String is a Data enclosed within quotes. It can be anything like text, numbers, special character, etc
#Strings are immutable that means, we can't change individual letters of a string
#String is represented by : " "

#Example

a = "Name" #Text
print(a)
b = "13" #Numbers
print(b)
c = "1.3" #Float
print(c)
d= "@&$^&*!!" #Special Characters
print(d)

##########################################################

#Indexing 

#Forward Indexing ->
#  0 1 2 3 4 5
# -------------  
# |P|Y|T|H|O|N|
# -6-5-4-3-2-1  <- Reverse Indexing

##########################################################

#Printing Multi Line String Data
#Example : 
s = '''Delhi
was previously known as
Indrapastha'''
print(s)

#Note : For making multi line string data, we need to use triple quotes

##########################################################

#Slicing of a String 
#Syntax : (Variable name[a,b-1])
#here, a = Starting value (Default = 0)
#b= End value 

print(a[0:2])
print(b[:1])
print(c[:])
print(d[0:4])

##########################################################

#Methods of String

print(a.capitalize()) #To Capitalize the first letter of a String
print(a.isalnum()) #To check, if all the elements given in the String is either alphabet or number
print(a.isalpha()) #To check, if all the elements given in the String is alphabet 
print(a.isdigit()) #To check, if all the elements given in the String is number
print(a.isspace) #To check, if there are any blank spaces between the String
print(a.islower()) #To check, if all the elements given in the String iare in lowercase
print(a.isupper()) #To check, if all the elements given in the String are in uppercase
print(a.istitle()) #To check, if all the elements given in the String have their first letter capitalized
print(a.lower()) #To Lower all the alphabets of the String
print(a.upper()) #To Capitalize all the alphabets of the String
print(a.title()) #To Capitalize first letter of each string
print(a.swapcase()) #Converts the upper case into lower case and the lower case into upper case of the String
print(a.partition("a")) #To break the string into differents parts based on an element ! It returns the String in 3 parts, that is before the seperator, the seperator(In this case, the seperator is "a") and after the seperator.










