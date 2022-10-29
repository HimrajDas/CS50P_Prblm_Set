import emoji

user_input = input("Input: ")
string = emoji.emojize(user_input, language='alias')
print(string)