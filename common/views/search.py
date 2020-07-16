import json

from django.http.response import JsonResponse
from rest_framework.views import APIView

from common.models.search import SearchTemplates
from common.utils.search_handler import generate_template, search_base_party


class SearchGetTemplateAPIView(APIView):

    def get(self, request, *args, **kwargs):
        template = generate_template()  # SearchTemplates.objects.all()
        return JsonResponse(template, safe=False)


class SearchBasePartyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        global search_result
        if request.data is not None:
            search_result = search_base_party(request.data)
        dummy_response = json.loads('{ "SearchResult":[ { "basePartyId": 1, "basePartyName": { "value": "Entity One", ' \
                                    '"icon": "autorenew", "color": "#008000" }, "legalId": "5366262", "sector": "Manufacturing", ' \
                                    '"systemSource": "Creditbase" }, { "basePartyId": 2, "basePartyName": { "value": "Entity ' \
                                    'Two", "icon": "autorenew", "color": "#FF5733" }, "legalId": "53636", "sector": "HEALTH", ' \
                                    '"systemSource": "Creditbase" }, { "basePartyId": null, "basePartyName": { "value": "Entity ' \
                                    'One", "icon": "autorenew", "color": "#008000" }, "legalId": "5366262", "sector": ' \
                                    '"undefined", "systemSource": "Host 1" }, { "basePartyId": null, "basePartyName": { "value": ' \
                                    '"Entity Four", "icon": "create", "color": "#FF5733" }, "legalId": "6262626", ' \
                                    '"sector": "undefined", "systemSource": "Host 1" }, { "basePartyId": null, "basePartyName": ' \
                                    '{ "value": "Entity Five", "icon": "create", "color": "#FF5733" }, "legalId": "73737373", ' \
                                    '"sector": "mining and hunting", "systemSource": "Host 1" } ], "ColumnConfig":[ { ' \
                                    '"headerName": "Full Name", "filter": "agTextColumnFilter", "filterParams": { ' \
                                    '"filterOptions": ["contains"] }, "field": "basePartyName", "action": "edit", ' \
                                    '"cellRenderer": "styleRenderer", "checkboxSelection": true }, { "headerName": "Legal ID", ' \
                                    '"filter": "agTextColumnFilter", "filterParams": { "filterOptions": ["contains"] }, ' \
                                    '"field": "legalId" }, { "headerName": "Sector", "filter": "agTextColumnFilter", ' \
                                    '"filterParams": { "filterOptions": ["contains"] }, "field": "sector" }, { "headerName": ' \
                                    '"Source", "filter": "agTextColumnFilter", "filterParams": { "filterOptions": ["contains"] ' \
                                    '}, "field": "systemSource", "rowGroup": true, "hide": true } ] } ')
        return JsonResponse(search_result, safe=False)
