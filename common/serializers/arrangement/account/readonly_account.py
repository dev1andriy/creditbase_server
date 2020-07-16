from rest_framework import serializers
from common.models.arrangement import Account, AccountRelatedParty
from common.models.general import PostingRestrictionType
from common.serializers.general.posting_restrictions_type import PostingRestrictionsTypeSerializer
from common.serializers.arrangement.account.account_related_parties import AccountRelatedPartiesSerializer


class ReadOnlyAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            "accountId": representation["AccountId"],
            "details": {
                "accountHighlights": {
                    "accountTitle": representation["AccountTitle"],
                    "accountOwner": representation["BasePartyId"]["BasePartyName"] if "BasePartyId" in representation and representation["BasePartyId"] is not None else None,
                    "accountId": representation["AccountId"],
                    "accountCategory": representation["AccountCategory"]["Description"] if "AccountCategory" in representation and representation["AccountCategory"] is not None else None,
                    "hostAccountId": representation["AccountIdHost"],
                    "accountType": representation["AccountType"]["Description"] if "AccountType" in representation and representation["AccountType"] is not None else None,
                    "editHostValues": representation["EditHostValuesFlag"] if "EditHostValuesFlag" in representation and representation["EditHostValuesFlag"] is not None else None,
                    "accountClass": representation["AccountClass"]["Description"] if "AccountClass" in representation and representation["AccountClass"] is not None else None,
                    "financialInstitution": representation["FinancialInstitution"]["Description"] if "FinancialInstitution" in representation and representation["FinancialInstitution"] is not None else None,
                    "currency": representation["Currency"]["Description"] if "Currency" in representation and representation["Currency"] is not None else None,
                    "businessUnit": representation["BusinessUnit"]["Description"] if "BusinessUnit" in representation and representation["BusinessUnit"] is not None else None,
                    "accountStatus": representation["AccountStatus"]["Description"] if "AccountStatus" in representation and representation["AccountStatus"] is not None else None,
                    "accountOfficer": representation["AccountOfficer"]["Description"] if "AccountOfficer" in representation and representation["AccountOfficer"] is not None else None,
                    "openDate": representation["OriginationDate"] if "OriginationDate" in representation and representation["OriginationDate"] is not None else None,
                    "lastTxnDate": representation["LastTransactionDate"] if "LastTransactionDate" in representation and representation["LastTransactionDate"] is not None else None,
                    "jointAccount": representation["JointAccountFlag"]["Description"] if "JointAccountFlag" in representation and representation["JointAccountFlag"] is not None else None,
                    "overdraftAllowed": representation["OverdraftAllowedFlag"]["Description"] if "OverdraftAllowedFlag" in representation and representation["OverdraftAllowedFlag"] is not None else None,
                    "liquidationAccount": representation["LiquidationAccountFlag"]["Description"] if "LiquidationAccountFlag" in representation and representation["LiquidationAccountFlag"] is not None else None,
                    "limitId": representation["LimitId"],
                    "lienMarked": representation["LienMarkedFlag"]["Description"] if "LienMarkedFlag" in representation and representation["LienMarkedFlag"] is not None else None,
                    "limitCurrency": representation["LimitCurrency"]["Description"] if "LimitCurrency" in representation and representation["LimitCurrency"] is not None else None,
                    "collateralizable": representation["CollateralizableFlag"]["Description"] if "CollateralizableFlag" in representation and representation["CollateralizableFlag"] is not None else None,
                    "limitAmount": representation["LimitAmount"],
                    'postingRestrictionType': PostingRestrictionsTypeSerializer(PostingRestrictionType.objects.filter(PostingRestrictionTypeId__in=representation['PostingRestrictionType']), many=True).data if representation['PostingRestrictionType'] is not None else None,
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
