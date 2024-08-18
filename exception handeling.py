try:
    num1 = int(input("Enter a number please: "))
    num2 = int(input("Enter another number please: "))
    print(num1/num2)

except ZeroDivisionError:
    print("You can't divide by zero! idiot! ")

except ValueError:
    print("Enter only number plz")

except Exception:
    print("Something went wrong :(")


else:
    print("This is all ok!")