# ignore the error of the diving 0 and 1
try:
    print(1/0)
# except statement for dividing by 0
except ZeroDivisionError:
    print("You cannot divide by zero")

try:
    x = int(input("Please enter a number: "))

# except state for entering values
except ValueError:
    print("Please enter a valid integer")

