from django.urls import path
from . import views

urlpatterns = [
    path('set_balance/', views.set_starting_balance, name='set_starting_balance'),
    path('add/', views.add_trade, name='add_trade'),
    path('', views.list_trades, name='list_trades'),
    path('close/<int:trade_id>/', views.close_trade, name='close_trade'),
    path('edit/<int:trade_id>/', views.edit_trade, name='edit_trade'),
    path('delete/<int:trade_id>/', views.delete_trade, name='delete_trade'),
    path('api/get-price/<str:token_pair>/', views.get_price, name='get_price'),
    path('fetch_historical_price/<str:symbol>/<str:date>/<str:time>/', views.fetch_historical_price_view, name='fetch_historical_price'),
]
