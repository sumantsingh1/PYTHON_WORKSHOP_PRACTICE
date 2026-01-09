day_of_week = input("Enter the day of week : ").lower() #convert lowercase
print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday": #true
    print("I will learn live devops")
else: #false
    print("I will pracitce Devops")

num1=int(input("Enter first Number : "))
num2=int(input("Enter second Number : "))

choice= input("Enter the operations : (Options + , - , * , / , % )")

if choice == "+":
    sum_of_num = num1 + num2
    print("Addition : ", sum_of_num)
elif choice == "-":
    diff_of_num = num1 - num2
    print("Subtractioin : ", diff_of_num)
elif choice == "*":
    mul_of_num = num1 * num2
    print("Multiplication : ", mul_of_num)
elif choice == "/":
    div_of_num = num1 / num2
    print("Division : ", div_of_num)
elif choice == "%":
    mod_of_num = num1 % num2
    print("Remainder : ", mod_of_num)
else :
    print("invalid choice") 
