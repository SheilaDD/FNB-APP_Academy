# control statements

# if statements
# if condition:
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false

# if condition1:
#     # code to execute if condition1 is true
# elif condition2:
#     # code to execute if condition2 is true
# else:
#     # code to execute if both conditions are false

num = 3

if num > 5:
    print("The number is positive.")
else:
    print("The number is negative.")

#multiple conditions
if num > 5:
    print("The number is greater than 5.")  
elif num == 5:
    print("The number is equal to 5.")  
else:
    print("The number is less than 5.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num1} is less than {num2}.") 
else:
    print(f"{num1} is equal to {num2}.")
