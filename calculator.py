print("Give a")
a = int(input())
print("Give b")
b = int(input())
print("Choose the type of calculation you would like to perform (+,-,*,/)")
type_of_calculation = input()

if(type_of_calculation == "+"):
    print("The result is " , (a+b))
elif(type_of_calculation == "-"):
    print("The result is " , (a-b))
elif(type_of_calculation == "*"):
    print("The result is " , (a*b))
elif(type_of_calculation == "/"):
    print("The result is " , (a/b))
else:
    print("Wrong input")


print(type((a/b)))    
