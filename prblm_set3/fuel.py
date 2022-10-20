def fuel():
    while True:
        try:
            pattern = input("Fraction: ")
            x, y = pattern.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                continue
            result = x / y
            result *= 100
            result = round(result)
            result = int(result)

        except (ValueError, ZeroDivisionError):
            pass
        else:
            if result <= 1:
                return "E"
            elif result >= 99:
                return "F"
            else:
                return f"{result}%"

print(fuel())
