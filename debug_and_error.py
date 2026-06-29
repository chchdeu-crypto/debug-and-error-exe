# #mission 1
# age = input("Enter your age: ")
# try:
#     next_year = int(age) + 1
#     print("Next year you will be", next_year)
# except ValueError:
#     print('enter only numbers')

# #mission 2
# a = int(input("First number: "))
# b = int(input("Second number: "))
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("cannot divide by zero")

# #mission 3
# numbers = [10, 20, 30]
# index = int(input("Choose index: "))
# try:
#     print(numbers[index])
# except IndexError:
#     print("index not found")

# #mission 4
# prices = {
#     "apple": 3,
#     "banana": 5
# }
# item = input("Enter item: ")
# try:
#     print(prices[item])
# except KeyError:
#     print("item not found")

#mission 5
# numbers = [100, 200, 300]
# try:
#     index = int(input("Choose index: "))
#     divider = int(input("Choose divider: "))
# except ValueError:
#     print("enter numbers")
# try:    
#     result = numbers[index] / divider
#     print(result)
# except IndexError:
#     print("index out of range")
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except NameError:
#     print("not ")
#mission 6
# try:
#     score = int(input("Enter score: "))
#     print("Your score is", score)
# except ValueError:
#     print("invalid score")
# finally:
#     print("check finished")

#mission 7
# name = input("Enter your name: ")
# if name == "admin":
#     print("Welcome admin")
# else:
#     print("Welcome user")
#because its not an error code

#missiom 8
price = 100
discount = 20
final_price = price - price / 100*discount
print(final_price)
#logic error
#it suppost to be 80 


