def main():
    question = input("What is the answer to the great question of life, the universe, and everything? ")
    deep_thought(question)


def deep_thought(question):
    match question:
        case '42' | 'forty-two' | 'forty two':
            print("yes")
        case _:
            print("what?")


main()