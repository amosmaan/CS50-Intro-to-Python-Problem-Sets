import json
import requests
import sys

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)
else:
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=e885c57542b2c6b5d739d9aa63644104ede78a523dd533d83f0f5f4b0edf6104",
            timeout=1,
        )
        page = response.json()
        mult = float(sys.argv[1])
        bitcoinprice = (float(page["data"]["priceUsd"])) * mult
        print(f"${bitcoinprice:,.4f}")
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    except requests.exceptions.RequestException:
        print("Request Error")
        sys.exit(1)
