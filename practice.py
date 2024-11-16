# list_1 = []
# i = 0
# while i < 5:
#     num = int(input("Enter number... "))
#     list_1.append(num)
#     i += 1
# list_1.sort()
# print("sorted list.. ", list_1, )
# even = []
# odd = []
# negative = 0
# positive = 0
# for no in list_1:
#     if no > positive:
#         positve = no
    
#     if no < negative:
#         negative = no

# print("Positive Value ...", positve)
# print("Negative Value ...", negative)
# for num in list_1:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#        odd.append(num)       
# print("Even list..", even)
# print("Even list..", odd)
#______________________________________
#factorial
# number = int(input("Enter positive number.. "))
# fact = 1
# i = 1
# while i <= number:
#     fact *= i
#     i += 1
# print("factorial ", fact)
#________________________________________
# #reversing a string
# digit = input("enter a string... ")
# string =""
# for i in digit:
#     string = i + string
# print(string)

#________________________________________
# Grading System
# grade = int(input("Enter your marks to know your Grade: "))
# if grade >= 90:
#     print("You got A Grade..")
# elif grade >= 80 < 90:
#     print("You got B Grade..")
# elif grade >= 70 < 80:
#     print("You got C Grade..")
# elif grade >= 60 < 70:
#     print("You got D Grade..")
# else:
#     print("You got F Grade..")
#________________________________________
# Even Odd Checker
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Number is  Even")
# else:
#     print("Number is Odd")
#________________________________________
# Number Guessing Game
import random
num = random.randint(1,50)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50.")
guess = None
while guess != num:
    try:
        guess = int(input("Enter your Guess .."))
        if guess < num:
            print("number you entered is too low..")
        elif guess > num:
            print("number you entered is too high..")
        else:
            print("Conrgats, you guess the Right Number!")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        