def main():
    user_str = input("Input: ").strip().lower()
    exclude_vowl(user_str)


def exclude_vowl(user_input):
    for letter in user_input:
        if not letter in ('a', 'e', 'i', 'o', 'u'):
            print(letter, end="")

            
main()