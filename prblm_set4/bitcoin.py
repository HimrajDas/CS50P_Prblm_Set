import sys
import requests
import json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if len(sys.argv) == 1:
    print("Missing command line argument!")
    sys.exit()
elif len(sys.argv) > 2:
    print("Number of arguments exceeded!")
else:
    try:
        amount = float(sys.argv[1])
    except ValueError:
        print("command line argument is not a number!")
    else:
        o = response.json()
        price = o["bpi"]["USD"]["rate_float"]
        print(price * amount)
