from django.http import HttpResponseBadRequest, JsonResponse
from rest_framework.views import APIView

from common.models import CurrencyRate


class GetCurrencyRateAPIView(APIView):

    def get(self, request, **kwargs):
        id = kwargs.get('id', None)

        if id is None:
            return HttpResponseBadRequest('Wrong currency id')

        currency_rates_array = CurrencyRate.objects.filter(CurrencyIn=id)
        currency_rates_dict = {
            '{}'.format(id): 1
        }

        for currency_rate in currency_rates_array:
            currency_rates_dict[currency_rate.CurrencyOut_id] = currency_rate.ExchangeRate

        return JsonResponse(currency_rates_dict)
