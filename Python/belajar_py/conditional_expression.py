#Date (1/1/26)


#Contional expression = Is a short one line for if-else statement (also known as ternary operator)
#                       Its contain 2 value and return a value based a condition
#                       Formula = "x" if "condition" else "y"

print("Please pick any number you want! (1 - 100 only)")

while True:
    num = int(input("Answer: "))
    num2 = int(input("Answer: "))
    if num <= 100 and num2 <= 100:
        break
    else:
        print("Please put your answer!")


import random
coin = random.randint(1, num)
coin = "Head" if coin % 2 == 0 else "Tail" 
print(coin)

result = "Even" if num % 2 == 0 else "ODD"
print(result)

age = "You're not old enough to ride this rollercoaster" if num <= 18 else "Age qualified! Enjoy your ride!"
print(age)

condition = "positive" if num > 0 else "Negative"
print("condition")












