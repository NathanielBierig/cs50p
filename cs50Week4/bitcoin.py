import requests
import sys
import json
import os

API_KEY = os.getenv("COINCAP_API_KEY") # internal
headers = {
    "Authorization": f"Bearer {API_KEY}"
}
try:
    if len(sys.argv)!= 2:
        raise ValueError
    amount = float(sys.argv[1])
    response = requests.get("https://rest.coincap.io/v3/price/bysymbol/BTC", headers=headers)
    response.raise_for_status()
    o = response.json()  
    price = float(o["data"][0])
    total = price * amount
    print(f"Price: ${total:,.4f} for {amount} Bitcoin")

except requests.RequestException as e:
    print(e)
    print("request error(with the api)")

except ValueError:
    print("Invalid bitcoin amount")