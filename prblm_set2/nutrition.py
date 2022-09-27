fruits_dic = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "kiwi": 90,
    "grape": 90,
    "lime": 20,
    "orange": 80,
    "pineapple": 50,
    "watermelon": 80,
}


fruit = input("Item: ").strip().lower()

if fruit in fruits_dic:
    print(f"Calorie: {fruits_dic[fruit]}")
else:
    print("No info.")
