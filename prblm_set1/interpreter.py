def main():
    expression = input("Expression: ")
    a, b, c = expression.split(" ")
    a = int(a)
    c = int(c)
    print(interpret(a, b, c))


def interpret(x, y, z):
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "/":
            return x / z
        case "*":
            return x * z
        case "%":
            return x % z
        case _:
            return "Enter valid information"


main()
