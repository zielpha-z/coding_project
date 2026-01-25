# Date (16/1/26)
# Tpic: WHILE LOOP
# while loop = exexecute some code While some condition remains true
# the while loop kida like if statement
name = input("Enter your name: ")
nama = name.capitalize()
alpha = name.isalpha()
print(alpha)

while not alpha:
    print("U didn't enter ur name: ")
    name = input("Enter your name: ")
    alpha = name.isalpha()
    nama = name.capitalize()

if nama == "Belva":
    print("Haiii, bel... Aku kangen kamu, ketemuan yuk")
else:
    print(f"Hello {name}")



# Date (16/1/26)
# Topic: FOR LOOP
# For loop = execytes a block of code a fixed number of time
#           you can iterate over a range, string, sequence, etc (anything considered iterabble)

# for <variabel> in <data cllection>:
    # the repeated block code

#EXample

#for x in range(1, 10, 2): 
    #print(x)

# The result is printed number begin with 1 and ended with 9 (the end/2nd vale is exclusive)
# And skipped/stepped by 2
# The x is variable (can be anything)
# And the range can be swapped with any iterabble data / collection of data
# such a as string, list, range, etc

# You can add reversed function
#for x in reversed(range(1, 10, 2)): 
    #print(x)

# Or you can add the ngeative 1 step, it does the same
for x in range(10, 1, -1): 
    print(x)
    print("selesai")

# So, the result is printed number start from 10 to 1 (reversed counting)













