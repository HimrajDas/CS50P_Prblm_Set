import random
import pyfiglet


game_name = pyfiglet.figlet_format("guess The Number")
print(game_name)

while True:
    try:
        level = int(input("Level: "))
        guess_number = int(input("Guess: "))
    except level < 0 or ValueError:
        continue
    else:
        rndm_number = random.randint(1, level)
        print(rndm_number)
        if guess_number > rndm_number:
            print("Too large!")
        elif guess_number < rndm_number:
            print("Too small!")
        else:
            print("Just right!")
        break
