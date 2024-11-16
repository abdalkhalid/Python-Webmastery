
def input_list():
    list_a = []
    for i in range(0,5):
        number = int(input("Enter a number: "))
        list_a.append(number)
    return list_a

def sum(list_a):
    sum = 0
    for i in list_a:
        sum += i
    return sum