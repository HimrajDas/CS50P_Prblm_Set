price = 50
recieved_amount = 0
print(f"Amount due: {price}")

while recieved_amount != price:
    user_amount = int(input("Insert coin: "))
    if user_amount == 25 or user_amount == 10 or user_amount == 5:
        recieved_amount += user_amount
        amount_due = price - recieved_amount
        if recieved_amount <= price:
            print(f"Amount due: {amount_due}")
        if recieved_amount >= price:
            change = recieved_amount - price
            print("Here's your coke.Enjoy!")
            print(f"Change owed: {change}")
            break
    else:
        print(f"Amount due: 50")
        continue
