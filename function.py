from django.db.models.expressions import result


def pilow(firstname, lastname):
    print(f"hii  {firstname} {lastname} brother welcome to our city")


pilow("Maruf","ahmed")


def multiply(number1, number2):
    result = number1 * number2
    return result


print(multiply(4,7))

