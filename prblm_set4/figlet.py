import pyfiglet
import sys

user_input = input("Input: ")
if len(sys.argv) == 1:
    txt_to_ascii = pyfiglet.figlet_format(user_input)
else:
    txt_to_ascii = pyfiglet.figlet_format(user_input, font=sys.argv[-1])
    
print(f"Output: \n{txt_to_ascii}")
