from datetime import datetime
print("Welcome to my AI chatbot.")
name=input("what's your name?\n")
print("Well then, nice to meet you", name.capitalize())
answer=input("How are you feeling?\n").lower()
good_synonyms = [
    "excellent", "great", "wonderful", "superb", "fantastic",
    "awesome", "amazing", "outstanding", "marvelous", "splendid",
    "terrific", "fabulous", "brilliant", "exceptional", "first-rate",
    "top-notch", "impressive", "admirable", "commendable", "fine",
    "positive", "superior", "pleasant", "delightful", "enjoyable",
    "satisfying", "nice", "lovely", "stellar", "remarkable"
]
bad_synonyms = [
    "awful", "terrible", "horrible", "dreadful", "poor", "inferior",
    "subpar", "unpleasant", "unacceptable", "lousy", "atrocious",
    "abysmal", "dire", "appalling", "nasty", "crummy", "shoddy",
    "defective", "faulty", "mediocre", "deplorable", "pathetic",
    "unsatisfactory", "disappointed", "unfortunate", "grim", "rotten",
    "vile", "wretched", "lamentable", "unfavorable", "objectionable"
]
if answer.startswith("not "):
  actual_word = answer[4:].strip()
  if actual_word == "good" or actual_word in good_synonyms:
    print("Hope you feel well soon :(")
  elif actual_word == "bad" or actual_word in bad_synonyms:
    print("I'm glad to here that!")
  else:
   print("I understand that feelings are sometimes impossible to express in the form of words. ")
else:
  if answer == "good" or answer in good_synonyms:
    print("I'm glad to here that!")
  elif answer == "bad" or answer in bad_synonyms:
    print("Hope you feel well soon :(")
  else:
   print("I understand that feelings are sometimes impossible to express in the form of words. ")
activities=input("What are you planning to do later on today?\n").capitalize()
print( activities ,"Sounds very fun!")
opinion=input("Are you excited? yes/no/maybe\n").lower()
if opinion == "yes":
  print("Keep the excitement going. You'll definitely enjoy it!")
elif opinion == "no":
  print("Don't be so sure, grumpypants, maybe you'll enjoy it.")
elif opinion == "maybe":
  print("Hope you enjoy it then :)")
else:
  print("I understand. Hope you enjoy it then.")
DateOfBirth=input("When is your birthday?(enter a date in numbers[DD/MM/YYYY])\n")
DateOfBirth=DateOfBirth.replace("/","")
while(not DateOfBirth.isnumeric()):
  DateOfBirth=input("Please re-enter your birthday(enter a date in numbers[DD/MM/YYYY])\n")
  DateOfBirth=DateOfBirth.replace("/","")
users_month_of_birth=DateOfBirth[2:4]
current_month=datetime.now().strftime("%m")
users_day_of_birth=DateOfBirth[0:2]
current_day=datetime.now().strftime("%d")
if users_month_of_birth == current_month:
  if users_day_of_birth == current_day:
   for i in range(3):
    print("\nHip Hip Hooray!")
   print("\nCongragulations!")
   print("\nHappy birthday!")
  elif users_day_of_birth>current_day:
   for i in range(3):
     print("\nHip Hip Hooray!")
   print("\nCongragulations!")
   print(DateOfBirth ,". A lucky day. Wish you a Happy Birthday in advance! ")
  elif users_day_of_birth<current_day:
     for i in range(3):
      print("\nHip Hip Hooray!")
     print("\nCongragulations!")
     print(DateOfBirth ,". A lucky day. Wish you a Belated Happy Birthday! ")
elif users_month_of_birth>current_month:
  for i in range(3):
    print("\nHip Hip Hooray!")
  print("\nCongragulations!")
  print(DateOfBirth ,". A lucky day. Wish you a Happy Birthday in advance! ")
elif users_month_of_birth<current_month:
  for i in range(3):
    print("\nHip Hip Hooray!")
  print("\nCongragulations!")
  print(DateOfBirth ,". A lucky day. Wish you a Belated Happy Birthday! ")
hobbies=input("And, just to socialize with you, what are your hobbies?")
print("Oh well",hobbies,",Sounds really fun.")
print("Nice talking to you. Chat to me sometime soon. Byeeeeeeeeeee!")