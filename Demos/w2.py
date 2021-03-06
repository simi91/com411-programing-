#program that display a menu and allows the user t ether see a nice message, calculate areas of renctagle or triangleor displaya times table for a number.

print("Please choose and option from the menu:\n\n1-Nice message\n2-Area of renctagle\n3-Area of tringle\n4-Times table")

option = int(input())

if option == 1:
  print("Today will be a good day")
elif option == 2:
  print("Enter the lengh of the renctagle:")
  l = int(input())
  print("Enter the width of the renctagle")
  w = int(input())
  area = w*1
  print("The area of this renctangle was {}" .format(area))
elif option == 3:
  print("Enter the base of triangle:")
  base = float(input())
  print("Enter the height of the triangle")
  height = float(input())
  area = 0.5*base*height
  print("The area of this triangle was {:.2f}" .format(area))
elif option == 4:
  print("What number would you like to see times table for?")
  n = int(input())
  for i in range(1,11,1):
    print("{}x{} = {}" .format(n,i,n*i))

else:
  print("There is not such option.Go to specsavers!")

