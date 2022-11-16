import random
import pyfiglet


game_name = pyfiglet.figlet_format("guess The Number")
print(game_name)

while True:
    try:
        level = int(input("Level: "))
        guess_number = int(input("Guess: "))
    except (ValueError, TypeError):
        continue
    except level < 0:
        continue
    else:
        rndm_number = random.randint(1, level)
        if guess_number > rndm_number:
            print("Too large!")
        elif guess_number < rndm_number:
            print("Too small!")
        else:
            print("Just right!")
        break
