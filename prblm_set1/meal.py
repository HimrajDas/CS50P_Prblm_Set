def main():
    time = input("What time is it? ")
    print(convert_time(time))


def convert_time(time):
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    minute /= 60
    minute = str(minute).lstrip("0.")
    current_time = float(f"{hour}.{int(minute)}")

    if 7 <= current_time <= 8:
        return "meal time"
    elif 12 <= current_time <= 13:
        return "lunch time"
    elif 18 <= current_time <= 19:
        return "dinner time"
    else:
        return 

main()

