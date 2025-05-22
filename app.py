from http_client import HttpClient as client

def convert_brl(amount, target_amount) -> float:
    return amount * target_amount
    


if __name__ == "__main__":
    # API key and base currency for the exchange rate API
    apiKey = "your_api_key_here"
    base_currency = "BRL"

    url = "https://v6.exchangerate-api.com/v6/" + apiKey + "/latest/" + base_currency
    
    data = {
        "base_code": base_currency,
        "currency_rates": {}
    }

    http_client = client()

    response = http_client.get_response(url)
    if response is None:
        print("Failed to fetch data from the API.")
        exit(1)

    data["currency_rates"] = response["conversion_rates"]
    
    while True:
        
        print("\n" + "-" * 50)
        amount = float(input("Enter the amount in BRL: "))
        target_currency = input("Enter the target currency: ").strip().upper()
        print("\n" + "=" * 50)
   
        
        if target_currency not in data["currency_rates"]:
            print("Invalid target currency.")
            print(f"Available currencies: {', '.join(data['currency_rates'].keys())}")
        else:
            print(f"Converting {amount} {base_currency} to {target_currency} at rate {convert_brl(amount, data['currency_rates'][target_currency])}")
        print("\n" + "*" * 50)
        choice = input("Do you want to convert another amount? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thank you for using the currency converter!")
            break
