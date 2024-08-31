from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Trade
from .forms import StartingBalanceForm, TradeForm, CloseTradeForm
from .utils import get_bybit_price
from django.http import JsonResponse
from .utils import fetch_historical_price as fetch_price
import requests
from datetime import datetime
import time
import logging

# View to set the starting balance
def set_starting_balance(request):
    profile, created = UserProfile.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = StartingBalanceForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('list_trades')  # Redirect to the main page after saving
    else:
        form = StartingBalanceForm(instance=profile)

    return render(request, 'trades/set_starting_balance.html', {'form': form})

# View to list all trades
def list_trades(request):
    profile = UserProfile.objects.first()
    trades = Trade.objects.all()
    return render(request, 'trades/list_trades.html', {'trades': trades, 'profile': profile})

# View to add a new trade
def add_trade(request):
    profile = UserProfile.objects.first()
    total_amount_required = 0
    percentage_of_balance = 0

    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            # Perform calculations
            token_pairing = form.cleaned_data['token_pairing']
            leverage_used = form.cleaned_data['leverage_used']
            position_size = form.cleaned_data['position_size']
            price = get_bybit_price(token_pairing)

            if price:
                total_amount_required = (position_size * price) / leverage_used
                percentage_of_balance = (total_amount_required / profile.starting_balance) * 100

            # Save the trade after calculations
            form.save()
            return redirect('list_trades')
    else:
        form = TradeForm()

    return render(request, 'trades/add_trade.html', {
        'form': form,
        'profile': profile,
        'total_amount_required': total_amount_required,
        'percentage_of_balance': percentage_of_balance
    })

# View to close a trade
def close_trade(request, trade_id):
    trade = get_object_or_404(Trade, id=trade_id)
    if request.method == 'POST':
        form = CloseTradeForm(request.POST, instance=trade)
        if form.is_valid():
            form.save()
            return redirect('list_trades')
    else:
        form = CloseTradeForm(instance=trade)
    return render(request, 'trades/close_trade.html', {'form': form, 'trade': trade})

# View to edit a trade
def edit_trade(request, trade_id):
    trade = get_object_or_404(Trade, id=trade_id)
    if request.method == 'POST':
        form = TradeForm(request.POST, instance=trade)
        if form.is_valid():
            form.save()
            return redirect('list_trades')
    else:
        form = TradeForm(instance=trade)
    return render(request, 'trades/edit_trade.html', {'form': form, 'trade': trade})

# View to delete a trade
def delete_trade(request, trade_id):
    trade = get_object_or_404(Trade, id=trade_id)
    if request.method == 'POST':
        trade.delete()
        return redirect('list_trades')
    return render(request, 'trades/delete_trade.html', {'trade': trade})

def get_price(request, token_pair):
    price = get_bybit_price(token_pair)
    return JsonResponse({'price': price})


def get_historical_price(symbol, date, timestamp):
    api_url = f"https://api.bybit.com/v2/public/kline/list?symbol={symbol}&interval=1&from={timestamp}"
    logging.debug(f"API URL: {api_url}")

    max_retries = 3
    retry_delay = 10  # Increase delay to avoid triggering the rate limit

    for attempt in range(max_retries):
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            logging.debug(f"API Response: {data}")

            if 'result' in data and data['result']:
                price = data['result'][0]['close']
                return price
            else:
                return None

        except requests.exceptions.HTTPError as e:
            logging.error(f"Request failed: {e}")
            if response.status_code == 429:  # Rate limit error
                logging.error("Rate limit exceeded. Retrying after delay...")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay * (attempt + 1))
                    continue
            return None

        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return None

        except ValueError as e:
            logging.error(f"JSON decode failed: {e}")
            return None
        
        
# View to fetch historical price
def fetch_historical_price_view(request, symbol, date, time):  # Ensure the parameter is named 'time'
    datetime_str = f"{date} {time}"
    try:
        dt_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        timestamp = int(dt_obj.timestamp())
    except ValueError as e:
        return JsonResponse({'error': 'Invalid date format'}, status=400)

    price = get_historical_price(symbol, date, timestamp)
    if price:
        return JsonResponse({'price': price})
    else:
        return JsonResponse({'error': 'Price not found'}, status=404)