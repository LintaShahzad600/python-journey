import requests
import sys
if len(sys.argv)!=2:
 sys.exit("Missing command-line argument")

try:
  n=float(sys.argv[1])
except ValueError:
   sys.exit("Command-line argument is not a number")

try:
    response=requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=3f3c3b627d1a18ad836cc637674d1fdba3c3c489e68cbfffc941ed8a26164b83")
    t=response.json()
    price=float(t["data"]["priceUsd"])
    total=n*price
    print(f"${total:,.4f}")
except requests.RequestException:
      sys.exit("API request failed")

