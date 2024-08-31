import requests
from datetime import datetime

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


def fetch_historical_price(symbol, date, time):
    # Convert date and time to UNIX timestamp
    timestamp = int(datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S").timestamp())
    interval = "1"  # 1-minute interval for precise time

    # Make the API request
    url = f"https://api.bybit.com/v2/public/kline/list?symbol={symbol}&interval={interval}&from={timestamp}"
    response = requests.get(url)
    data = response.json()

    # Check if the response contains the expected data
    if response.status_code == 200 and 'result' in data and data['result']:
        # Get the close price of the first candle
        historical_price = data['result'][0]['close']
        return historical_price
    else:
        return None