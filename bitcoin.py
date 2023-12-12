






import requests
import sys

try:
    n_bitcoin=float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response=response.json()
    price=(response["bpi"]["USD"]["rate_float"])
    amount=price * n_bitcoin
    print(f"${amount:,.4f}")
except ValueError:
    sys.exit("Command-line artugment is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
    
except requests.RequestException:
     sys.exit("RequestException")