from rest_framework import serializers
from common.models.arrangement import Account


class AccountsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            "accountId": representation["AccountId"],
            "accountTitle": representation['AccountTitle'],
            "basePartyName": representation["BasePartyId"]["BasePartyName"] if "BasePartyId" in representation and representation["BasePartyId"] is not None else None,
            "hostAccountId": representation["AccountIdHost"],
            "accountType": representation["AccountType"]["Description"] if "AccountType" in representation and representation["AccountType"] is not None else None,
            "businessUnit": representation["BusinessUnit"]["Description"] if "BusinessUnit" in representation and representation["BusinessUnit"] is not None else None,
            "currency": representation["Currency"]["Description"] if "Currency" in representation and representation["Currency"] is not None else None,
            'accountStatus': {
                "value": representation['AccountStatus']['Description'] if 'AccountStatus' in representation and representation['AccountStatus'] is not None else None,
                "icon": representation['AccountStatus']['Description1'] if 'AccountStatus' in representation and representation['AccountStatus'] is not None else None,
                "color": representation['AccountStatus']['Description2'] if 'AccountStatus' in representation and representation['AccountStatus'] is not None else None
            },
            "dateOpened": representation["OriginationDate"],
            "balanceDate": representation["BalanceDate"]
        }

        return to_represent
