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
    price = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=391619dfa2f915830f535d636d671755471b5a37673f9f6802809a96f0af8b37")
    price.raise_for_status()
except requests.HTTPError:
    sys.exit("request failed")
else:
    o = price.json()
    amt = float(o["data"]["priceUsd"])
    btc = n * amt
    print(f"${btc:,.4f}")


