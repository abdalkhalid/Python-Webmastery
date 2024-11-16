# a = input("enter a first number ")
# b = input("enter a second number ")
# def Sum(val1, val2 ):
#     global a
#     global b
#     a = input("enter a local number  ")
#     b = input("enter a local number  ")
#     localsum =int(a)+int(b)
#     print("Sum for Local Variables.. " , localsum)
#     globalsum  = int(a)+int(b)
#     return globalsum
# globalsum  = Sum(a, b)
# print("Sum for Global Variavles.. ", globalsum)
import module_implement

_name = input("Enter your name.. ")
print(module_implement.greet(_name))