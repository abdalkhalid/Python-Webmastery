# list_1 = []
# for i in range(0, 5):
#     inp = int(input("Enter a number: "))
#     list_1.append(inp) 
#     i += 1

#input from user and append to list
list_1 = [] 
for i in range(0, 5):
    inp = int(input("Enter a number: "))
    list_1.append(inp) 
    i += 1

i = 0 
while i < len(list_1):
    j = i +1
    while j < len(list_1):
        if list_1[i] == list_1[j]:
           del list_1[j]
        else:
            j += 1
    i += 1
print(list_1)










