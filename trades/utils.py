import requests

def get_bybit_price(token_pair):
    url = f"https://api.bybit.com/v2/public/tickers?symbol={token_pair}"
    response = requests.get(url)
    
    # Print the raw response content for debugging
    print(f"API Response Status Code: {response.status_code}")
    print(f"API Response Content: {response.text}")
    
    try:
        data = response.json()
        if 'result' in data and data['result']:
            price = float(data['result'][0]['last_price'])
            return price
    except ValueError as e:
        print("Error decoding JSON:", e)
    
    return None
