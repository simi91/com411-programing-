#we wish to create a program that allow us to specify what type of book is being read by beep
#program should start by asking the user to enter the type of book e.g adventure

print("please enter the first whole number")
n=int(input())
print ("please enter the second whole number")
m=int(input())
print("please enter the third number")
p=int(input())
x=0
y=0
if(n%2==0)
  x=x+1
else:
  y=y+1
if(m%2==0)
  x=x+1
else:
  y=y+1
if(p%2==0)
  x=x+1
else:
  y=y=1
print("There were {} even numbers and {} add numbers".format(x,y))
