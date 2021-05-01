#Sean Tay
#ITP 449
#HW1

#1.Write a program that prompts the user to enter a password then prints the length of the password
#i = input("Enter your password: ")
#print("Your password is", len(i), "long.")

#2.Write a program that prompts the user to enter their full name then prints the number of characters in their name (do not count spaces)
#i = input("What is your name? ")
#print(i, "your name has", (len(i) - i.count(" ")), "characters.")

#3. Write a program that prompts the user to enter a month (as a number), then prints the name of the month and the number of days in that month. Ensure that the user inputs a valid month and handle any error cases.
i = True
while i:
  try:
    i = int(input("Enter the month number: "))
  except ValueError:
    print("This is not a number.")
    continue
  else:
    if i==1:
      print("January has 31 days")
      break
    elif i==2:
      print("February has 28 days")
      break
    elif i==3:
      print("March has 31 days")
      break
    elif i==4:
      print("April has 30 days")
      break
    elif i==5:
      print("May has 31 days")
      break
    elif i==6:
      print("June has 30 days")
      break
    elif i==7:
      print("July has 31 days")
      break
    elif i==8:
      print("August has 31 days")
      break
    elif i==9:
      print("September has 30 days")
      break
    elif i==10:
      print("October has 31 days")
      break
    elif i==11:
      print("November has 30 days")
      break
    elif i==12:
      print("December has 31 days")
      break
    else:
      print("Invalid month number. Please try again.")

#4. Write a program that prompts the user to enter a loan amount, annual interest rate, and number of years for a car loan. Then calculate and print the monthly payment amount.
PV = float(input("Loan Amount: "))
i = float(input("Annual Interest Rate: "))
n = float(input("Years: "))
ii = (i/100.0)/12.0
nn = n*12.0
pmt = (PV*ii*((1+ii)**nn))/(((1+ii)**nn)-1)
print("Your monthly payment is: $" + str(format(pmt, '.2f')))

#5. Write a program to that prompts the user to enter a string. Then check whether or not the string is a palindrome
l = input("Enter a string: ")
w = ""
for i in l.lower():
  w = i + w
if (l.lower() == w):
  print("Yes")
else:
  print("No")

#6. Write a program to compute and print all possible combinations of change for $1. Denominations to be considered – quarter, dime, nickel, penny.
#Hint: Use nested loops (loops within loops for the various denominations of coins
print("Change for $1:")
for quarter in range(0,5):
  for dime in range(0,11):
    for nickel in range(0,21):
      for penny in range(0,101):
        if(penny + 5*nickel + 10*dime + 25*quarter == 100):
          print(quarter, "quarters,", dime, "dimes,", nickel, "nickels,", penny, "pennies" )

#7. Ask the user to enter two positive integers between 1 and 100. Read those integers. Then output a multiplication table of the first number times the second number.
#Note: You have to ensure the entered numbers are between 1 and 100 only.
continueThis = True
continueThis2 = True
while continueThis:
    pos = int(input("Please enter an integer: "))
    while pos < 1 or pos > 100:
        pos = int(input("Please enter an integer: "))
    else:

        continueThis = False
while continueThis2:
    pos2 = int(input("Please enter another integer: "))
    while pos2 < 1 or pos2 > 100:
        pos2 = int(input("Please enter another integer: "))
    else:
        continueThis2 = False

if (pos > 0 and pos < 101) and (pos2 > 0 and pos2 < 101):
    for i in range(1, pos2 + 1):
        c = pos * i
        print(pos, "x", i, "=", c)

#8. Write a program to ask the user to enter a password. Then check to see if it is a valid password based on these requirements -
#Must be at least 8 characters long
#Must contain both uppercase and lowercase letters
#Must contain at least one number between 0-9
#Must contain a special character -!,@,#,$
#If the password is not valid, ask the user to re-enter. This should continue until the user enters a valid password. After a valid password is entered, print Access Granted!

continueThis = True
while continueThis:
  password = input("Please enter a password. Follow these requirements - \n a. Must be at least 8 characters long \n b. Must contain both uppercase and lowercase letters \n c. Must contain at least one number between 0-9 \n d. Must contain a special character -!,@,#,$ ")
  if len(password) < 8:
    print("Password:", password)
    print("Invalid password. Try again!")
  elif not any(i.isupper() for i in password):
    print("Password:", password)
    print("Invalid password. Try again!")
  elif not any(i.islower() for i in password):
    print("Password:", password)
    print("Invalid password. Try again!")
  elif not any(i.isdigit() for i in password):
    print("Password:", password)
    print("Invalid password. Try again!")
  elif not any(not i.isalnum() for i in password):
    print("Password:", password)
    print("Invalid password. Try again!")
  else:
    print("Password:", password)
    print("Access Granted!")
    break

#9. Given the score sheet of participants in a competition, you are required to find the runner-up score. You are given scores in a list. Find the score of the runner-up.
n = int(input())  # runner up
array = map(int, input().split()) # mapping input to int
array = list(set(list(array)))  #converts the arrary to a list, gets the list's set, and converts it into a list.
array2 = len(array)
array = sorted(array)
print(array[array2-2])
