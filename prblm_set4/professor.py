import random

def main():
    count = 10
    score = 0
    level = get_level()
    while count > 0:
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        ans = num1 + num2
        





def get_level():
    return int(input("Level: "))


def generate_integer(level):
    if level == 1:
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10, 99)
    elif level == 3:
        integer = random.randint(100, 999)
    return integer


if __name__ == "__main__":
    main()
