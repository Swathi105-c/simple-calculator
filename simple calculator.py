
def Addition (num1,num2):
    return num1+num2
def Substraction (num1,num2):
    return num1-num2
def Multiplication (num1,num2):
    return num1*num2
def Division (num1,num2):
    return num1/num2

print('Enter two number for calculator')

num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))

print("Enter your choice \n 1.Addition \n 2.Subtraction \n 3.Division \n 4. Multiplication")
choice=int(input())


if choice == 1:
    # addition
    print("Addition",Addition(num1,num2)) 
elif choice ==2:
    #substraction
    print("Substraction",Substraction(num1,num2))
elif choice==3:
    #division
    print("Division",Division(num1,num2))
elif choice==4:
    #multiplication
    print("Multiplication",Multiplication (num1,num2))
