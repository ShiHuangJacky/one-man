# if(6 >= 7):
#     print("bye bye fatty")
# else:
#     print("ni hao")

# expression = "bye bye fatty" if 6>=7 else "ni hao"
# print(expression)

# sale = False
# store_message = "Hello we have a sale today" if sale else "We don't have a sale today"
# print(store_message)

# store_message = ""
# sale = True
# if(sale):
#     print("We have sale")
# else:
#     print("no sale")
# print(store_message)

# if(2**2 == 4) and (4**2 == 8):
#     print("true")
# else:
#     print("false")

# if ((not(2**3 == 8)) or (4**2 == 8)):
#     print("true")
# else:
#     print("false")

# def add_two_if_even_and_add_three_if_three(travis_scott_burger):
#     if(travis_scott_burger % 2 == 0):
#         return travis_scott_burger + 2
#     elif(travis_scott_burger == 3):
#         return travis_scott_burger + 3
#     return travis_scott_burger
# x = 1
# y = 2
# z = 3
# print(add_two_if_even_and_add_three_if_three(x))
# print(add_two_if_even_and_add_three_if_three(y))
# print(add_two_if_even_and_add_three_if_three(z))

try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a/b)
except ZeroDivisionError:
    print("b was equal to zero, computers can't divide by zero")
    b = int(input("b: "))
    print(a/b)
