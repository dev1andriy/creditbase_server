from django.urls import path

from common.views.arrangements import accounts as accounts_views
from common.views.arrangements import account_related_parties as account_related_parties_views
from common.views.arrangements import facility as facility_views
from common.views.arrangements import collateral as collateral_views
from common.views.arrangements import coverages as coverages_views
from common.views.arrangements import deposit as deposit_views

urlpatterns = [
    path('Arrangements/Accounts', accounts_views.AccountsAPIView.as_view(), name='Arrangements-Accounts'),
    path('Arrangements/Accounts/<int:id>', accounts_views.AccountsAPIView.as_view(), name='Arrangements-Accounts'),

    path('Arrangements/Account', accounts_views.AccountAPIView.as_view(), name='Arrangements-Account'),
    path('Arrangements/Account/<int:id>', accounts_views.AccountAPIView.as_view(), name='Arrangements-Account'),

    path('Arrangements/AccountRelatedParty/<int:id>', account_related_parties_views.AccountRelatedPartyAPI.as_view(), name='Arrangements-AccountRelatedParty'),


    path('Arrangements/Facilities', facility_views.FacilitiesAPIView.as_view(), name='Arrangements-Facilities'),
    path('Arrangements/Facilities/<int:id>', facility_views.FacilitiesAPIView.as_view(), name='Arrangements-Facilities'),

    path('Arrangements/Facility', facility_views.FacilityAPIView.as_view(), name='Arrangements-Facility'),
    path('Arrangements/Facility/<str:model>/<int:id>', facility_views.FacilityAPIView.as_view(), name='Arrangements-Facility'),

    path('Arrangements/Facility/Archive/<str:model>/<int:id>', facility_views.FacilityArchiveAPIView.as_view(), name='Arrangements-Facility-Archive'),

    path('Arrangements/Facility/GetParameters', facility_views.FacilityGetParametersAPIView.as_view(), name='Arrangements-Facility-GetParameters'),


    path('Arrangements/Collaterals', collateral_views.CollateralsAPIView.as_view(), name='Arrangements-Collaterals'),
    path('Arrangements/Collaterals/<int:id>', collateral_views.CollateralsAPIView.as_view(), name='Arrangements-Collaterals'),

    path('Arrangements/Collateral', collateral_views.CollateralAPIView.as_view(), name='Arrangements-Collateral'),
    path('Arrangements/Collateral/GetCoverageData/<int:id>', collateral_views.CollateralGetCoverageDataAPIView.as_view(), name='Arrangements-Collateral'),
    path('Arrangements/Collateral/<str:model>/<int:id>', collateral_views.CollateralAPIView.as_view(), name='Arrangements-Collateral'),

    path('Arrangements/Collateral/Archive/<str:model>/<int:id>', collateral_views.CollateralArchiveAPIView.as_view(), name='Arrangements-Collateral-Archive'),

    path('Arrangements/Collateral/GetParameters', collateral_views.CollateralGetParametersAPIView.as_view(), name='Arrangements-Collateral-GetParameters'),


    path('Arrangements/Deposits', deposit_views.DepositsAPIView.as_view(), name='Arrangements-Deposits'),
    path('Arrangements/Deposits/<int:id>', deposit_views.DepositsAPIView.as_view(), name='Arrangements-Deposits'),

    path('Arrangements/Deposit', deposit_views.DepositAPIView.as_view(), name='Arrangements-Deposit'),
    path('Arrangements/Deposit/<str:model>/<int:id>', deposit_views.DepositAPIView.as_view(), name='Arrangements-Deposit'),

    path('Arrangements/Deposit/Archive/<str:model>/<int:id>', deposit_views.DepositArchiveAPIView.as_view(), name='Arrangements-Deposit-Archive'),

    path('Arrangements/Deposit/GetParameters', deposit_views.DepositGetParametersAPIView.as_view(), name='Arrangements-Deposit-GetParameters'),

    path('Arrangements/Coverages/<int:id>', coverages_views.CoveragesAPIView.as_view(), name='Arrangements-Coverages'),

    path('Arrangements/Coverage/Archive/<str:model>/<int:id>', coverages_views.CoverageArchiveAPIView.as_view(), name='Arrangements-Coverage-Archive'),

    path('Arrangements/Coverage/<str:bind>/<str:model>/<int:id>', coverages_views.CoverageAPIView.as_view(), name='Arrangements-Coverage'),
    path('Arrangements/Coverage/<str:bind>/<str:model>', coverages_views.CoverageAPIView.as_view(), name='Arrangements-Coverage'),
    path('Arrangements/Coverage/<str:bind>', coverages_views.CoverageAPIView.as_view(), name='Arrangements-Coverage'),


    path('Arrangements/CoverageGetConfig/<str:bind>/<str:model>/<int:id>', coverages_views.CoverageGetConfigAPIView.as_view(), name='Arrangements-Coverage-Get-Config')

]
