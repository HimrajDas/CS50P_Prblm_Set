file_formats = ".gif .png .txt .jpeg .jpg .zip .txt"


def main():
    file_name = input("File name: ").lower()
    print(show_folder(file_name))


def show_folder(file_name):
    global file_formats
    folder = "images"
    file = file_name.split(".")
    if file[-1] in file_formats:
        return f"{folder}/{file[-1]}"
    else:
        return "application/octet-stream"


main()
