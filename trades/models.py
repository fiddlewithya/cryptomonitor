from django.db import models
from .token_pairings import TOKEN_PAIRINGS  # Importing the pairings

class UserProfile(models.Model):
    starting_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"Starting Balance: {self.starting_balance} USDT"

class Trade(models.Model):
    POSITION_TYPES = [
        ('Long', 'Long'),
        ('Short', 'Short'),
    ]

    RESULT_TYPES = [
        ('TP', 'Take Profit'),
        ('SL', 'Stop Loss'),
        ('Cancelled', 'Cancelled'),
    ]

    TIMEFRAME_CHOICES = [
        ('1min', '1 minute'),
        ('5min', '5 minutes'),
        ('15min', '15 minutes'),
        ('30min', '30 minutes'),
        ('1hr', '1 hour'),
        ('4hr', '4 hours'),
        ('8hr', '8 hours'),
        ('1day', '1 day'),
    ]

    date = models.DateField(default='2024-08-30')  # Set a default date value
    time = models.TimeField(default='00:00')  # Set a default time value
    token_pairing = models.CharField(max_length=19, choices=TOKEN_PAIRINGS)  # Load choices from the external file
    leverage_used = models.IntegerField()
    position_size = models.DecimalField(max_digits=20, decimal_places=8)
    position_type = models.CharField(max_length=5, choices=POSITION_TYPES)
    strategy_type = models.CharField(max_length=100)
    timeframe = models.CharField(max_length=10, choices=TIMEFRAME_CHOICES)
    opening_notes = models.TextField(blank=True, null=True)
    
    pnl = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    result = models.CharField(max_length=10, choices=RESULT_TYPES, blank=True, null=True)
    percentage_change = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    closing_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.token_pairing} | {self.date} {self.time} | {self.position_type}"
