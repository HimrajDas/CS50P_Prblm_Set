def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    num_str = ""
    if s[:2].isalpha():
        if 2 <= len(s) <= 6:
            if not s[(len(s) - 1) // 2 : (len(s) + 2) // 2].isdigit():
                for m in s:
                    if m.isdigit():
                        num_str += m
                        if not num_str.startswith("0"):
                            for i in s:
                                if not i in  "! @ # $ % ^ & * ( ) _ - + =".split():
                                    return True


main()
