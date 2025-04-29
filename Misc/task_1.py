
# # # Getting input from user
# # first_number = input("Enter the first Number..")
# # second_number = input("Enter the second Number..")

# # # inupt is String by default converting into integers
# # sum = int(first_number) + int(second_number)
# # print("Sum = ", sum )

person_1 = int(input("Person 1 age: "))
person_2 = int(input("Person 2 age: "))
if person_1 > person_2:
        if person_1 >= 18:          
             print("Person 1 is Adult and Elder")           
        else:           
             print("Person 1 is Minor but Elder")
elif person_1 < person_2:  
     if person_2 >= 18:      
        print("Person 2 is Adult and Elder")      
     else:   
            print("Person 2 is Minor but Elder")  
else:
    if person_1 and person_2 >= 18:
        print("Both are adult age fellows..")  
    else:
        print("Both are Minor and age Fellows..")
