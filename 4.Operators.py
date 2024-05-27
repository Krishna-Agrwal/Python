#Order of Precendence of Operators
#Highest -> Lowest down the group

#|----------------|---------------------------------------------------------|
#|  Operator      |     Description                                         |
#|----------------|---------------------------------------------------------|
#|  ()            | Parenthesis /Brackets                                   |  
#|  **            | Exponential or Power                                    |
#|  ~             | nor                                                     |
#|  +, -          | Positive, Negative                                      |
#|  *, /, //, %   | Multiplocation, Division, Floor Division, Remainder     |
#|  +, -          | Additon, Substraction                                   |
#|  &             | AND                                                     |
#|  |             | OR                                                      |
#|  <, >          | Greater, Smaller                                        |
#|  <=, >=        |Greater and equal, Smaller and equal                     |
#|  !=, ==        | Not Equal/Same, Equal/Same                              |
#|  is, isnot     |                                                         |
#|  not           |                                                         |
#|  and           | Satisfy Both the Condition                              |
#|  or            | Satisfy any one of the Condition                        |
#|----------------|---------------------------------------------------------|


#Arithmetic Operators
#--------------------

num1 = 10
num2 = 2

print("num1 + num2 :", num1+num2) #Addition
print("num1 - num2 :", num1-num2) #Substraction
print("num1 * num2 :", num1*num2) #Multiplication
print("num1 / num2 :", num1/num2) #Division (To get the complete quotient of the divison)
print("num1 ** num2 :", num1**num2) #Power (Square the Value)
print("num1 // num2 :", num1//num2) #Floor Division(To get the quotient in the integer form)
print("num1 % num2 :", num1%num2) #Modulus (To get the remainder of a division)

#Assignment Operators
#--------------------

a = 15
#Here, "=" is a assignment operator because it helps to assign a value to the variable

#Arithmetic Operation with Assignment Operator
#----------------------------------------------

a+= 10 #Additon
print(a) 
a-= 10 #Substraction
print(a) 
a*= 10 #Multiplication
print(a) 
a/= 10 #Division
print(a) 

#Comparison Operator
#--------------------

x = 10
y = 5

print(x>y) #Greater than
print(x<y) #Smaller than
print(x==y) #Equal value
print(x!=y) #Values are not equal
print(x>=y) #Greater than and equal to
print(x<=y) #Smaller than and equal to

#Logical Operator
#-----------------

k = 15
z = 10

#1. AND Operator : To check if both the conditons are true
print(k==z and k>z)
#It will return true, if both the conditons satisfy

#OR Operator : To check if any one of the condition is true
print(k==z or k>z)
#It will return true, if any one of the conditon is true

#NOT Operator : Reverse the output
print(not(True))
print(not(False))