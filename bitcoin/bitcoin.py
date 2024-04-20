import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        bitcoin_data = response.json()
        return bitcoin_data['bpi']['USD']['rate_float']
    except (requests.RequestException, KeyError):
        sys.exit("Failed to fetch Bitcoin price data")

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    bitcoin_price = get_bitcoin_price()
    total_cost = bitcoins * bitcoin_price

    formatted_cost = "${:,.4f}".format(total_cost)
    print(formatted_cost)

if __name__ == "__main__":
    main()
