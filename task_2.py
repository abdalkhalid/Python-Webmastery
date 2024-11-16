ages = []
j = 0
while j < 5:
      age = int(input("enter a number.. "))
      ages.append(age)
      j += 1
limit = 18
for i in (ages):
    if i > limit :
            print(f"{i} is greater than {limit} ")
    elif i < limit :
            print(f"{i} is less than {limit} ")
    else:
        print(f"{i} is equal to {limit}")
        print("If Else ended")
   







