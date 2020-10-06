# def large_power(base, exponent):
#     if(base**exponent > 5000):
#         return True
#     else:
#         return False
# print(large_power(2, 13))
# print(large_power(2,12))

# def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
#     if(budget < food_bill + electricity_bill + internet_bill + rent):
#         return True
#     else:
#         return False
# print(over_budget(100, 20, 30, 10, 40))
# print(over_budget(80, 20, 30, 10, 30))

# def twice_as_large(num1, num2):
#     if(num1 > num2*2):
#         return True
#     else:
#         return False
# print(twice_as_large(10,5))
# print(twice_as_large(11,5))

# def divisible_by_ten(num):
#     if(num % 10 == 0):
#         return True
#     else:
#         return False
# print(divisible_by_ten(20))
# print(divisible_by_ten(25))

def not_sum_to_ten(num1, num2):
    if(num1 + num2 != 10):
        return True
    else:
        return False
print(not_sum_to_ten(9,1))
print(not_sum_to_ten(5,5))