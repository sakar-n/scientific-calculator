def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("select operation")
print("1. for add")
print("2. for substract")
print("3. for multiply")
print("4. for divide")

while True:
    choice = input("enter your choice(1/2/3/4):")
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("enter 1st number : "))
        num2 = float(input("enter 2nd number : "))
    elif choice == "1":

        print(add( num1 , num2))
    elif choice == "2":
        print(substract( num1, num2))
    elif choice == "3":
        print(multiply( num1, num2))
    elif choice == "4":
        print(divide( num1, num2))
    break
else:
    print("invalid input")

