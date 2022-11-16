import random


def main():
    score = 0
    level = get_level()
    for i in range(10):
        chance = 3
        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y
        while True:
            try:
                user_ans = int(input(f"{x} + {y} = "))
                break
            except ValueError:
                chance -= 1
                if chance == 0:
                    print(ans)
                    break
                print("EEE")
                continue
        if user_ans != ans:
            while user_ans != ans:
                try:
                    chance -= 1
                    if chance == 0:
                        print(ans)
                        break
                    print("EEE")
                    user_ans = int(input(f"{x} + {y} = "))
                except ValueError:
                    chance -= 1
                    print("EEE")
        if user_ans == ans:
            score += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            continue


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
