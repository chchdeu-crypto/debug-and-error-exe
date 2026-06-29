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
# price = 100
# discount = 20
# final_price = price - price / 100*discount
# print(final_price)
#logic error
#it suppost to be 80 

#misison 9
# password = "abc123"
# guess = input("Enter password: ")

# if guess == password:
#     print("Login successful")
# else:
#     print("Wrong password")
#The bug is that if I enter the wrong code it logs me in.

#misison 10
# num1 = int(input("Number 1: "))
# op = input("Operator: ")
# num2 = int(input("Number 2: "))
# try:
#     num1 = int(input("Number 1: "))
#     op = input("Operator: ")
#     num2 = int(input("Number 2: "))
#     if op == "+":
#         print(num1 + num2)
#     elif op == "-":
#         print(num1 - num2)
#     elif op == "*":
#         print(num1 * num2)
#     elif op == "/":
#         print(num1 / num2)
#     else:
#         print("unknowm operetor")
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("enter numbers")
# finally:
#     print("calculator closed")

#part 2
#mission 1
# try:
#     celsius = input("Celsius: ")
#     fahrenheit = int(celsius) * 9 / 5 + 32
#     print(fahrenheit)
# except ValueError:
#     print("temp must be a number")

#misison 2
# word = input("Enter word: ")
# try:
#     print(word[0])
# except IndexError:
#     print("word is empty")

#mission 3
# scores = [90, 80, 100]
# total = 0

# for score in scores:
#     total += score

# average = total / len(scores)
# print(average)

#output 33.33
#logig error
#print(total)=100

#mission 4
# products = {
#     "pen": 4,
#     "notebook": 12
# }
# product = input("Product: ")
# try:
#     amount = int(input("Amount: "))
# except ValueError:
#     print("enter numbers")
# try:
#     print(products[product] * amount)
# except KeyError:
#     ("not found index")

#mission 5
# files = ["data.txt", "users.csv", "notes.txt"]
# try:
#     choice = int(input("Choose file number: "))
#     print(files[choice])
# except IndexError:
#     print("out of tange")
# except ValueError:
#     print("enter numbers")

#misison 6
# numbers = [4, 10, 2, 8]
# maximum = 0

# for number in numbers:
#     if number > maximum:
#         maximum = number

# print(maximum)
#output=0
#expected output=10

#misison 7
# user = {
#     "name": "Dana",
#     "age": 25
# }

# field = input("Choose field: ")
# try:
#     print(user[field].upper())
# except AttributeError:
#     print("cannot upper numbers")
# except KeyError:
#     print("key not exzist")

#mission 8
try:
    price = int(input("Price: "))
    amount = int(input("Amount: "))
    total = price * amount
    total_after_disc=total
    if amount > 3:
        total_after_disc = total*0.9

    print(total_after_disc)

except ValueError:
    print("enter only numbers")

