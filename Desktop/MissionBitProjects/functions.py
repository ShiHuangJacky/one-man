# def greet_customer(special, sale_percent):
#     print("Hello")
#     print("Our special today is " + special)
#     print("Everything is " + sale_percent + "off today.")
#     print("have a great time shopping!")

# greet_customer("peanut butter", "99% ")

# def add_one(num):
#     return num + 1

# x = add_one(1)
# print(x)


# def add_two(num):
#     return num + 2


# def greet_customer(special):
#     return "Our special today is " + special
# print(greet_customer("banana yogurt"))

# def add_one_if_odd(num):
#     if num % 2 != 0:
#         return num + 1
#     else:
#         return num

z = 10

def square_point_plus_ten(x, y):
    x_2 = x*y + z
    y_2 = y*y + z
    return x_2, y_2
x_squared, y_squared = square_point_plus_ten(2,4)
print(str(x_squared) + " " +str(y_squared))
