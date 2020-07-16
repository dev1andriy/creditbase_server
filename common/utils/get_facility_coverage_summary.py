from common.models import Facility, Collateral, Coverage
from common.utils.return_value_or_none import return_value_or_none

def get_facility_coverage_summary(facility_id):
    if facility_id is None:
        return

    facility = Facility.objects.filter(FacilityId=facility_id).first()

    facility_exposure_total = {
        'host_value': return_value_or_none(facility.ExposureTotal, 'HostValue'),
        'proposed_value': return_value_or_none(facility.ExposureTotal, 'ProposedValue'),
    }

    open_market_value = {
        'host_value': 0,
        'proposed_value': 0
    }
    discounted_value = {
        'host_value': 0,
        'proposed_value': 0
    }
    forced_sale_value = {
        'host_value': 0,
        'proposed_value': 0
    }

    coverages = Coverage.objects.filter(FacilityId=facility_id)

    for coverage in coverages:
        if coverage.CollateralId is not None:
            collateral = coverage.CollateralId

            lien_order = coverage.LienOrder
            assignment = coverage.Assignment
            if assignment is not None and lien_order is not None:
                open_market_value['host_value'] = (open_market_value.get('host_value') + ((return_value_or_none(collateral.MarketValue, 'HostValue')) if lien_order == 1 else (return_value_or_none(collateral.MarketValue, 'HostValue') * assignment)) if return_value_or_none(collateral.MarketValue, 'HostValue') is not None and isinstance(return_value_or_none(collateral.MarketValue, 'HostValue'), float or int) else 0)
                open_market_value['proposed_value'] = (open_market_value.get('proposed_value') + ((return_value_or_none(collateral.MarketValue, 'ProposedValue')) if lien_order == 1 else (return_value_or_none(collateral.MarketValue, 'ProposedValue') * assignment)) if return_value_or_none(collateral.MarketValue, 'ProposedValue') is not None and isinstance(return_value_or_none(collateral.MarketValue, 'ProposedValue'), float or int) else 0)

                discounted_value['host_value'] = (discounted_value.get('host_value') + ((return_value_or_none(collateral.DiscountedValue, 'HostValue')) if lien_order == 1 else (return_value_or_none(collateral.DiscountedValue, 'HostValue') * assignment)) if return_value_or_none(collateral.DiscountedValue, 'HostValue') is not None and isinstance(return_value_or_none(collateral.DiscountedValue, 'HostValue'), float or int) else 0)
                discounted_value['proposed_value'] = (discounted_value.get('proposed_value') + ((return_value_or_none(collateral.DiscountedValue, 'ProposedValue')) if lien_order == 1 else (return_value_or_none(collateral.DiscountedValue, 'ProposedValue') * assignment)) if return_value_or_none(collateral.DiscountedValue, 'ProposedValue') is not None and isinstance(return_value_or_none(collateral.DiscountedValue, 'ProposedValue'), float or int) else 0)

                forced_sale_value['host_value'] = (forced_sale_value.get('host_value') + ((return_value_or_none(collateral.ForcedSaleValue, 'HostValue')) if lien_order == 1 else (return_value_or_none(collateral.ForcedSaleValue, 'HostValue') * assignment)) if return_value_or_none(collateral.ForcedSaleValue, 'HostValue') is not None and isinstance(return_value_or_none(collateral.ForcedSaleValue, 'HostValue'), float or int) else 0)
                forced_sale_value['proposed_value'] = (forced_sale_value.get('proposed_value') + ((return_value_or_none(collateral.ForcedSaleValue, 'ProposedValue')) if lien_order == 1 else (return_value_or_none(collateral.ForcedSaleValue, 'ProposedValue') * assignment)) if return_value_or_none(collateral.ForcedSaleValue, 'ProposedValue') is not None and isinstance(return_value_or_none(collateral.ForcedSaleValue, 'ProposedValue'), float or int) else 0)

    coverage_by_omv = {
        'host_value': (open_market_value.get('host_value') / facility_exposure_total.get('host_value')) if facility_exposure_total.get('host_value') is not None and open_market_value.get('host_value') != 0 else None,
        'proposed_value': (open_market_value.get('proposed_value') / facility_exposure_total.get('proposed_value')) if facility_exposure_total.get('proposed_value') is not None and open_market_value.get('proposed_value') != 0 else None
    }
    coverage_by_dv = {
        'host_value': (discounted_value.get('host_value') / facility_exposure_total.get('host_value')) if facility_exposure_total.get('host_value') is not None and discounted_value.get('host_value') != 0 else None,
        'proposed_value': (discounted_value.get('proposed_value') / facility_exposure_total.get('proposed_value')) if facility_exposure_total.get('proposed_value') is not None and discounted_value.get('proposed_value') != 0 else None
    }
    coverage_by_fsv = {
        'host_value': (forced_sale_value.get('host_value') / facility_exposure_total.get('host_value')) if facility_exposure_total.get('host_value') is not None and forced_sale_value.get('host_value') != 0 else None,
        'proposed_value': (forced_sale_value.get('proposed_value') / facility_exposure_total.get('proposed_value')) if facility_exposure_total.get('proposed_value') is not None and forced_sale_value.get('proposed_value') != 0 else None
    }

    return [
        {'parameterGroup': 'Exposure Info', 'parameter': 'Facility Limit', 'facility': True, 'hostValue': return_value_or_none(facility.CommitmentValue, 'HostValue'), 'proposedValue': return_value_or_none(facility.CommitmentValue, 'ProposedValue')},
        {'parameterGroup': 'Exposure Info', 'parameter': 'Outstanding Balance', 'facility': True, 'hostValue': return_value_or_none(facility.BalanceValue, 'HostValue'), 'proposedValue': return_value_or_none(facility.BalanceValue, 'ProposedValue')},
        {'parameterGroup': 'Exposure Info', 'parameter': 'Total Exposure', 'facility': True, 'hostValue': facility_exposure_total.get('host_value', None), 'proposedValue': facility_exposure_total.get('proposed_value', None)},
        {'parameterGroup': 'Collateral Info', 'parameter': 'Open Market Value (OMV)', 'collateral': True, 'hostValue': open_market_value.get('host_value', None), 'proposedValue': open_market_value.get('proposed_value', None)},
        {'parameterGroup': 'Collateral Info', 'parameter': 'Discounted Value (DV)', 'collateral': True, 'hostValue': discounted_value.get('host_value', None), 'proposedValue': discounted_value.get('proposed_value', None)},
        {'parameterGroup': 'Collateral Info', 'parameter': 'Forced Sale Value (FSV)', 'collateral': True, 'hostValue': forced_sale_value.get('host_value', None), 'proposedValue': forced_sale_value.get('proposed_value', None)},
        {'parameterGroup': 'Coverage Ratios', 'parameter': 'Coverage By OMV', 'collateral': True, 'hostValue': coverage_by_omv.get('host_value', None), 'proposedValue': coverage_by_omv.get('proposed_value', None)},
        {'parameterGroup': 'Coverage Ratios', 'parameter': 'Coverage By DV', 'collateral': True, 'hostValue': coverage_by_dv.get('host_value', None), 'proposedValue': coverage_by_dv.get('proposed_value', None)},
        {'parameterGroup': 'Coverage Ratios', 'parameter': 'Coverage By FSV', 'collateral': True, 'hostValue': coverage_by_fsv.get('host_value', None), 'proposedValue': coverage_by_fsv.get('proposed_value', None)}
    ]