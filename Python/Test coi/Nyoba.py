# Write code below 💖
import random

quest = str(input("What questionts do you want to ask? "))


answer = random.randint(1, 20)
final = 0

if answer == 1:
  final = "Yes - definitely."
elif answer == 2:
  final =  "It is decidedly so."
elif answer == 3:
  final =  "Without a doubt."
elif answer == 4:
  final =  "Reply hazy, try again."
elif answer == 5:
  final =  "Ask again later."
elif answer == 6:
  final =  "Better not tell you now."
elif answer == 7:
  final =  "My sources say no."
elif answer == 8:
  final =  "If you can goon 10 times a day. The answer is yes!."
elif answer == 9:
  final = "Hell nah brow."
elif answer == 10:
  final = "Aye, better wake up from that dream."
elif answer == 11:
  final = "Just kill your self li'l nig."
elif answer == 12:
  final = "Maybe."
elif answer == 13:
  final = "Just accept that fate bro. Why askin'?"
elif answer == 14:
  final = "Bro, you're cooked."
elif answer == 15:
  final = "It can happen, with hard workin muscle."
elif answer == 16:
  final = "Ain't gonna lie dude, you definately got it!"
elif answer == 17:
  final = "Cheer up, you can do it!"
elif answer == 18:
  final = "That's answer is yes."
elif answer == 19:
  final = "Stfu nigga. No!."
else:
  final = "Very doubtful bro."

print('Questions: ' + quest)
print('Magic 8 Ball: ' + final)

#print (f"final = {final}")