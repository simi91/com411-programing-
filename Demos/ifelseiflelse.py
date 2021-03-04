print("What is yor name?")
n = input()
# print("Do yu have a dog? (type True or False)")
# dog = input()
# #bool is boolean dataypes - nly store True/False


if len(n) >= 9: #allow lenght of exactly 9 and greater
   print("You have a very loooong name!")
   print("Your name contains {} letters". format(len(n)))
elif len(n) > 6:
  print("Your name is a bit long.Consider a nickname")
elif len(n) <3:
  print("Your name is veeeeery short") 
else:
  print("Your name is quite okay")
print("This is the END of the program!")