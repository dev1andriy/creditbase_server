from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view
from django.utils import timezone
from main.common.camel_case_parser import CamelCaseParser
from common.models.other.recent_item import RecentItem
from common.models.base_party import *
from common.serializers import BasePartiesSerializer


@api_view(['GET'])
@ensure_csrf_cookie
def get_recent_items(request, item_type):
    try:
        item_type = int(item_type)
    except:
        return HttpResponseBadRequest("Wrong item type ( it must be a number )")

    if item_type == 1:
        to_response = []
        recent_items = RecentItem.objects.filter(ItemType=item_type).order_by('-LastUpdatedDate')
        for item in recent_items:
            try:
                to_response.append(
                    CamelCaseParser.to_camel_case_single(
                        BasePartiesSerializer(BaseParty.objects.get(BasePartyId=item.ItemKey)).data))
            except:
                pass
            if len(to_response) >= 10:
                break

        return JsonResponse(to_response, safe=False)
    return HttpResponseNotFound("Wrong item type")


def set_recent_item(item_type, item_key, user):
    item_type = int(item_type)
    item_key = int(item_key)

    try:
        existing_recent_item = RecentItem.objects.get(ItemType=item_type, ItemKey=item_key)
        existing_recent_item.LastUpdatedDate = timezone.now()
        existing_recent_item.save()
    except ObjectDoesNotExist:
        recent_item = RecentItem()
        recent_item.ItemType = item_type
        recent_item.ItemKey = item_key
        recent_item.InsertDate = timezone.now()
        recent_item.LastUpdatedDate = timezone.now()
        recent_item.save()

    return HttpResponse(200)
