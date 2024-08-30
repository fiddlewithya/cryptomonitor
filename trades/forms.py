from django import forms
from .models import Trade, UserProfile
from django.db import models

class TradeForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'step': 1}))  # 24-hour format
    leverage_used = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'range', 'min': 1, 'max': 100, 'id': 'leverage_slider'}))  # Slider from 1x to 100x
    position_size = forms.DecimalField(widget=forms.NumberInput(attrs={'step': '0.1'}))  # Number input with step
    timeframe = forms.ChoiceField(choices=Trade.TIMEFRAME_CHOICES)  # Dropdown for timeframe
    opening_notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))  # Adjusting the textarea size

    class Meta:
        model = Trade
        exclude = ['pnl', 'result', 'percentage_change', 'closing_notes']

    def __init__(self, *args, **kwargs):
        super(TradeForm, self).__init__(*args, **kwargs)
        self.fields['opening_notes'].label = "Opening Notes"

class CloseTradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['pnl', 'result', 'percentage_change', 'closing_notes']  # Include only the closing fields

class StartingBalanceForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['starting_balance']      

