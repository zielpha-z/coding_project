#Date (31/12/25)


#*Mini prject, pythagoras teorem
import sys
import math
import time

base = 0
hypotenuse = 0
height = 0

def print(text, time_delay=0.1, tenses_pause=1.8):
    alpha = len(text)
    for wordd in text:
        sys.stdout.write(f"{wordd}")
        sys.stdout.flush()
        time.sleep(time_delay)
    time.sleep(tenses_pause)
    sys.stdout.write("\n")
   

def base_func(height, hypotenuse, base, answer):
    if answer == "base":
        result = math.sqrt((pow(hypotenuse, 2)) - (pow(height, 2)))
        return result
    elif answer == "height":
        result = math.sqrt((pow(hypotenuse, 2)) - (pow(base, 2)))
    else:
        result = math.sqrt((pow(base, 2)) + (pow(height, 2)))
    return result


print("Hello, welcome to my simple pythagoras solver!")
print("Triangle has 3 sides, the base, height and hypotenuse")
print("So, choose any one side whichever you like to find!")
print("Just write down your answer (use undercase only and make sure you to not typo)")

#qanswer = bool(answer)

while True:
    answer = input("Answer: ")
    if answer == "base":
        print("Hmmhm... Seems you choose the base")
        print("Pick any number for the height!")
        height = float(input("Answer: "))
        print("Aight then, gimme the hypotenuse!")
        hypotenuse = float(input("Answer: "))
        result = base_func(height, hypotenuse, base, answer)
        break
    elif answer == "height":
        print("Ohhh, i see, you chose the height!")
        print("Give me any number of base!")
        base = float(input("Answer: "))
        print("And for the hypotenuse too!")
        hypotenuse = float(input("Amswer: "))
        result = base_func(height, hypotenuse, base, answer)
        break
    elif answer == "hypotenuse":
        print("Good choice! You picked the hypotanuse aren't ya?")
        print("Aight, gimme any number for the  base!")
        base = float(input("Answer: "))
        print("And... Ofcourse the height too!")
        height = float(input("Answer: "))
        result = base_func(height, hypotenuse, base, answer)
        break
    else:
        print("Come on bro, be serious!!!")
        print("Try again!")


print(f"You chose the {answer}...")
print("Wait, before i give u the result...")
print("Do you want the result to be rouded by 2 decimal places? (y/n) ")
des = input("Answer: ")

while True:
    if des == "y":
        print("Okayy, gimme a sec,")
        result = round(result, 2)
    elif des == "n":
        print("Okay, if you don't want to,")
    else:
        print("Answer is not valid! Use 'y' for yes and 'n' for no")


print(f"Aandd... the result is...")
print("Thanks!")
