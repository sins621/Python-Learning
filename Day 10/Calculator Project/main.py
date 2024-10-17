import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


print(art.logo)
SIGNS = """+
-
*
/"""

calculating = "y"
while calculating != "q":
    result = 0
    while calculating == "y":
        if result != 0:
            n1 = result
        else:
            n1 = float(input("What's the first number?:"))
        print(SIGNS)
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        result = calculator[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
        calculating = input(
            f"Type 'y' to continue calculating with {result},"
            " type 'n' to start a new calculation,"
            " or type 'q' to quit the program. \n"
        ).lower()
