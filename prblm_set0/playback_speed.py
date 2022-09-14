def main():
    string = input("Say: ").rstrip()
    print(playback(string))


def playback(say):
    return f"{say.replace(' ', '...')}"


main()
