# date 2/1/26
nama = "Diaz"   # <--- this is string, a data type when u squeeze value in colons

result = len(nama) # <--- A functiion taht tells how many charactes that in a string (including the space too)
result = nama.find("d") #T hat func find any character you assign and returned the order of it (if python cant find it, it'll give -1) start from 0
result = nama.rfind("a")  # an opposite from .find, it search the order from the las character in string (start from 0, 1, 2, etc) 
result = nama.upper()   # To uppercase all character in a string in akphabet
result = nama.lower()   # To loer =case all the alphbet in a string
result = nama.capitalize()  # to mkake the string first charcter uooercase
result = nama.isdigit()  # to check a condition if the string are all digits and returned the value in boolean (space is exceptable)
result = nama.isalpha()   # to chack if tje characters are all the alphabet (space is excluded) and returned the value in boolean
result = nama.count("b")  # to count the given charactr 
result = nama.replace("a", "b")  # to replace the character in to aother
#print(result)
#print(help(str))



# Date (15/1/26)
# indexing = accesing elements of a sequence using [] ---> (indexing operator)
#           [start : end : step]

# Indexing
credit_number = "1234-5678-9012=3456" #the first indexing number start from 0 from the left of the string

result = credit_number[0] #answer = 1
# starting index number start from character 1 to begin from thr left
result = credit_number[0:4] #answer = 1234
# the end index is exclusive
# the end index is taking 4 characters with the start begin with character indexing number 0 (the first character)
# until the character with indexing number 3 (the fourth caracter in srring) b
# bevause the end indexing value is exclusive, the character with indexing number 4 doesn't indlude
result = credit_number[:4] 
# same as this, python will assume that start index value is set 0 (start from first character from the left ) 
result = credit_number[5:9] #the answer is 5678. 
# the start index value is inclusive
# The start index indexing number starts from 0 (the firs character from the right)
# until the character with indexing number 5 (the sixt characther from the right)
# and taking 4 characters, start from character with 5 indexing number until 8 indexing number
result = (credit_number[5:]) #answer = 5678-9012-3456
# python will assume that u wants all the character until its end 
result = (credit_number[-1]) #answer = 6
# indexing start from the last character on string (reverse direction = start from the right) 

# step index step the index by the given value
result = credit_number[::2]
# that's give us the second character within our string
# and that two colon with empty value, python will assume that we want our string from the very beginning until the last character 
result = credit_number[::-1] #the result = credit card number in reverse
# step the strings's character in reverse direction (this start from the right)
result = credit_number[:5]
print(result)



# Date (16/1/26)
# format specifiers (when use in context of an f strings):
# {your_value:flags} = they allow us to format the value 
#                      based on what flags are inserted 
# the flags are called a format specifiers

# EXAMPLE:

price1 = 1.2345
price2 = -278.3
price3 = 12.55

# .(number)f = round to that many decimal places (fixed point)
result1 = (f"price 1 is ${price1:.2f}") #result = 1.23
result2 = (f"price 2 is ${price2:.2f}") #result = -278.30 (python added 0 to make 2 decimal places)
result3 = (f"price 3 is ${price3:.2f}") #result = 12.55

# :(number) = allocates that many spaces to display values
result1 = (f"price 1 is ${price1:10}") #result =    1.2345
result2 = (f"price 2 is ${price2:10}") #result =    -278.3
result3 = (f"price 3 is ${price3:10}") #result =     12.55
# the values have total 10 space to display the output.
# if the characters are all have their spaces, the leftover empty spaces become spaces character

# :03 = aloocate and zero pad in that many leftover empty spaces
result1 = (f"price 1 is ${price1:010}") #result = 00001.2345
result2 = (f"price 2 is ${price2:010}") #result = -0000278.3
result3 = (f"price 3 is ${price3:010}") #result = 0000012.55

# :< = left justify
result1 = (f"price 1 is ${price1:<10}") 
result2 = (f"price 2 is ${price2:<10}") 
result3 = (f"price 3 is ${price3:<10}") 
# the result same as :(number) flag, but the value is justify to the right
# and all the empty spaces are swaps to the end of the string (again, the empty spaces are form as character spaces)

# :> = right justify
result1 = (f"price 1 is ${price1:>10}") 
result2 = (f"price 2 is ${price2:>10}") 
result3 = (f"price 3 is ${price3:>10}") 
# the reuslt iscsame as :< flag, it justify the value to the right
# instead the empty spaces are in the end, they locate in front of the value (left)

# :^ = center align
result1 = (f"price 1 is ${price1:^10}") 
result2 = (f"price 2 is ${price2:^10}") 
result3 = (f"price 3 is ${price3:^10}") 
# the result = the values are centered and squeze beetwen the empty spaces

# :+ = use a plus sign to indicates positive value
result1 = (f"price 1 is ${price1:+}") 
result2 = (f"price 2 is ${price2:+}") 
result3 = (f"price 3 is ${price3:+}") 
# the result = the values are displayed with a plus sign in front of the value if the value was positive
#             and negative sign if the value was negative

# :  = insert a space cahacter before positive numbers
result1 = (f"price 1 is ${price1: }") #result = 1.2345
result2 = (f"price 2 is ${price2: }") #result =-278.3
result3 = (f"price 3 is ${price3: }") #result = 12.55

# := = use equal sign to left most position
result1 = (f"price 1 is ${price1:=}") 
result2 = (f"price 2 is ${price2:=}") 
result3 = (f"price 3 is ${price3:=}") 
# idk what this flag even do

# :, = to add coma separater
price1 = 12345.12345
result1 = (f"price 1 is ${price1:,}") #result = 12,345.12345
price2 = -2009.3007
result2 = (f"price 2 is ${price2:,}") #result = -2,009.3007
price3 = 2009.2709
result3 = (f"price 3 is ${price3:,}") #result = 2,009.2708

# Ofc, u can combine/mixed these flags to format the strings!
result1 = (f"price 1 is ${price1:+,.2f}") #result =+12,345.12
result2 = (f"price 2 is ${price2:+,.2f}") #result =-2,009.30
result3 = (f"price 3 is ${price3:+,.2f}") #result =+2,009.27

print(result1)
print(result2)
print(result3)









