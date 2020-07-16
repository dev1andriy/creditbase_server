from rest_framework import serializers
from common.models.arrangement import Account, AccountRelatedParty
from common.serializers.arrangement.account.account_related_parties import AccountRelatedPartiesSerializer


class EditAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            "accountId": representation["AccountId"],
            "details": {
                "accountHighlights": {
                    "accountTitle": representation["AccountTitle"],
                    "accountOwner": representation["BasePartyId"],
                    "accountId": representation["AccountId"],
                    "accountCategory": representation["AccountCategory"],
                    "hostAccountId": representation["AccountIdHost"],
                    "accountType": representation["AccountType"],
                    "editHostValues": representation["EditHostValuesFlag"],
                    "accountClass": representation["AccountClass"],
                    "financialInstitution": representation["FinancialInstitution"],
                    "currency": representation["Currency"],
                    "businessUnit": representation["BusinessUnit"],
                    "accountStatus": representation["AccountStatus"],
                    "accountOfficer": representation["AccountOfficer"],
                    "openDate": representation["OriginationDate"],
                    "lastTxnDate": representation["LastTransactionDate"],
                    "jointAccount": representation["JointAccountFlag"],
                    "overdraftAllowed": representation["OverdraftAllowedFlag"],
                    "liquidationAccount": representation["LiquidationAccountFlag"],
                    "limitId": representation["LimitId"],
                    "lienMarked": representation["LienMarkedFlag"],
                    "limitCurrency": representation["LimitCurrency"],
                    "collateralizable": representation["CollateralizableFlag"],
                    "limitAmount": representation["LimitAmount"],
                    "postingRestrictionType": representation["PostingRestrictionType"],
                    "order": representation["OrderingRank"],
                    "print": representation["PrintFlag"],
                },
                "relatedParties": AccountRelatedPartiesSerializer(AccountRelatedParty.objects.filter(AccountId=representation["AccountId"]).order_by('OrderingRank'), many=True).data,
                "balanceInformation": {
                    "bookBalance": representation['BalanceBook'],
                    "availableBalance": representation['BalanceAvailable'],
                    "balanceDate": representation['BalanceDate']
                }
            }
        }

        return to_represent
