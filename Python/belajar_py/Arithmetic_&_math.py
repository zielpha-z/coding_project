#Date (31/12/25)
#Basic Arithmetic expression

friends = 6
addition = 4 + 2 
friends += 1          #<---- The augmented assigment operator (The shortened one!)
#print(addition)

substraction = friends - 1
friends -= 1
#print(substraction)

multiplication = 4 * 2
friends *= 1
#print(multiplication)

division1 = 4 / 2 #If u use the "/", the result will be a float (decimal) type not an int (whole number)
friends /= 1 
#print(division1)
#print(type(division1))

division2 = 4 // 2
friends //= 1
#print(division2)
#print(type(division2))

eksponentiation = 4 ** 2   #<---- Use "**" instead for eksponen expression
friends **= 2
#print(eksponentiation)

modulus = friends % 2 #<---- the "%" sign is modulus/modules idk. That's give u the remainder of any division!
friends %= 2 
#print(modulus)         #The answer is 1, as 2 number only fit 2 timesin 5. And the left space is 1
#print(friends)

f1 = 3.55
f2 = 3.45
f3 = 13.85
f4 = 451

i1 = 2
i2 = -3
i3 = 4

#result = round(f4)         #A function, To rounded decimal value to the nearest int number. Only works for float type!
#print(result)

#result = abs(f1)           #Absolute function use togive the absolute number of value (the distance away the value has from zero)
#result = pow(i3, i1)        #To do a exponential operasion with the base number at first place and the exponen located at second

#result = max(f1, f2, f3, f4, i1, i2, i3)   #To search max value at various values
#result = min(f1, f2, f3, f4, i1, i2, i3)   #To search min value at various values

import math #Import masth module from python directory, with this we can use advanced math expression 

#print(math.pi) 
#print(math.e)

#result = math.sqrt(i3)   #To find square root of a value
#result = math.ceil(f2)    #To always round up float digits
#result = math.floor(f1)   #To always round down float digits
#print(result)


#*Mini prject, pythagoras teorem

base = 0
hypotenuse = 0
height = 0

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





