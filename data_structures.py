#  List manipulation
# _______________________________
# num = input("Enter five numbers seprated by spaces: ")
# list_1 = []
# for i in num.split():
#     list_1.append(int(i))
# print("List: ", list_1)
# maximum = max(list_1)  
# print("Maximum: ", maximum)
# count = 0
# for i in list_1:
#     if i == maximum:
#         count += 1 
# print("Maximum occred ", count, " times") 
# if count == 1:
#     print("Maximum not repeated")
# print(co
# numbers = input("enter numbers with spaces: ")
# numbr_list = []
# for i in numbers.split():
#     numbr_list.append(int(i))
# for i in numbr_list:
#     if i == 0:
#         numbr_list.remove(i)
# print(numbr_list)
# j = 0
# for i in numbr_list:
#     if i %2 == 0:
#         numbr_list.remove(i)
# print(numbr_list) # numbers = input("enter numbers with spaces: ")
#  numbr_list = []
#  check = input("Enter a number to check..")
#  count = 0
#  for i in numbers.split():
#      numbr_list.append(int(i))
#      if i == check:
#          count += 1
#  print("NUmber appeared ", count, " times in list")

# # Tuple Manipulatoin
# # _______________________________
# import random
# tuple_1 = ()
# tuple_1 = tuple(random.randint(1, 100) for _ in range(10))
# print("Tuple: ", tuple_1)
# user_input = int(input("Enter a number to check: "))
# count = tuple_1.count(user_input)
# print(f"Number {user_input} appeared {count} times in Tuple")

# countries = ("USA", "Canada", "Mexico", "Pakistan")
# capitals = ("Washington, D.C.", "Ottawa", "Mexico City", "Islamabad")
# populations = (331, 38, 128, 212)
# main_tuple = (countries, capitals, populations)
# for i in range(len(main_tuple)):
#     print(f"The capital of {main_tuple[0][i]} is {main_tuple[1][i]} and it has a population of {main_tuple[2][i]} million people.") 
 
#  Dictionary Manipulation
# ______________________________
phone_book ={}
def add_contact(name, number):
    if name in phone_book:
        print("Contact exists")
    else:
        phone_book[name] = number
def update_contact(name, number):
    if name in phone_book:
        phone_book[name] = number
    else:
        print("Contact not found")
def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
    else:
        print("Contact not found")
def search_contact(name):
    if name in phone_book:
        print(f"Name: {name}, Number: {phone_book[name]}")
    else:
        print("Contact not found")
while True:
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
    elif choice == 2:
        name = input("Enter name: ")
        number = input("Enter number: ")
        update_contact(name, number)
    elif choice == 3:
        name = input("Enter name: ")
        delete_contact(name)
    elif choice == 4:
        name = input("Enter name: ")
        search_contact(name)
    elif choice == 5:
        break
    else:
        print("Invalid choice")

# Set Manipulation
# _______________________________
# Student Club Memberships
# computer_club = {"John", "Jack", "Jill", "Joe"}
# math_club = {"Jack", "Sam", "Sue", "Sally"}
# belogs_to_both = computer_club.intersection(math_club)
# print("Members of both clubs: ", belogs_to_both)
# student_only_in_one_club = computer_club.symmetric_difference(math_club)
# print("Members of only one club: ", student_only_in_one_club)
# atleast_one_club = computer_club.union(math_club)
# print("Members of atleast one club: ", atleast_one_club)
# only_computer_club = computer_club.difference(math_club)
# print("Members of only computer club: ", only_computer_club)

