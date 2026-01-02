#date 2/1/26



nama = "Diaz"   #<--- this is string, a data type when u squeeze value in colons

print("What's ur name bro?")
nama = input("Answer: ")

result = len(nama) #<--- A functiion taht tells how many charactes that in a string (including the space too)
result = nama.find("d") #That func find any character you assign and returned the order of it (if python cant find it, it'll give -1) start from 0
result = nama.rfind("a")  #an opposite from .find, it search the order from the las character in string (start from 0, 1, 2, etc) 
result = nama.upper()   #To uppercase all character in a string in akphabet
result = nama.lower()   #To loer =case all the alphbet in a string
result = nama.capitalize()  #to mkake the string first charcter uooercase
result = nama.isdigit()  #to check a condition if the string are all digits and returned the value in boolean (space is exceptable)
result = nama.isalpha()   #to chack if tje digits all the alphabet (space is excluded) and returned the value in boolean
result = nama.count("b")  # to count the given charactr 
result = nama.replace("a", "b")  #to replace the character in to aother



print(result)
print(help(str))



