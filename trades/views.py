from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Trade
from .forms import StartingBalanceForm, TradeForm, CloseTradeForm
from .utils import get_bybit_price
from django.http import JsonResponse
from .utils import get_bybit_price


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