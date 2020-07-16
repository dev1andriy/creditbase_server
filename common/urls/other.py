from django.urls import path
from common.views import recent_item as recent_item_view
from common.views.note import update_note
from common.utils.currency_rates import GetCurrencyRateAPIView

urlpatterns = [
    path('RecentItems/<int:item_type>', recent_item_view.get_recent_items, name='RecentItems'),

    path('Note', update_note, name="Note"),

    path('GetCurrencyRates/<int:id>', GetCurrencyRateAPIView.as_view(), name='GetCurrencyRates')
]
