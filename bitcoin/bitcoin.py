import sys
import requests
import json
if len(sys.argv) == 1:
        sys.exit("No argument found")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Argument not a number")
try:
    price = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=")
    price.raise_for_status()
except requests.HTTPError:
    sys.exit("request failed")
else:
    o = price.json()
    amt = float(o["data"]["priceUsd"])
    btc = n * amt
    print(f"${btc:,.4f}")


