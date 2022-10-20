def fuel():
    while True:
        try:
            pattern = input("Fraction: ")
            x, y = pattern.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                continue
            formula = x / y
            answer = f"{str(formula).strip('0.')}%"
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if x == y:
                return "F"
            elif x == 0:
                return "E"
            else:
                return answer

print(fuel())
