from common.models import Facility, Collateral, Coverage
from common.utils.return_value_or_none import return_value_or_none

def get_collateral_coverage_summary(collateral_id):
    if collateral_id is None:
        return

    collateral = Collateral.objects.filter(CollateralId=collateral_id).first()

    open_market_value = {
        'host_value': return_value_or_none(collateral.MarketValue, 'HostValue'),
        'proposed_value': return_value_or_none(collateral.MarketValue, 'HostValue')
    }

    discounted_value = {
        'host_value': return_value_or_none(collateral.MarketValue, 'HostValue'),
        'proposed_value': return_value_or_none(collateral.MarketValue, 'HostValue')
    }

    forced_sale_value = {
        'host_value': return_value_or_none(collateral.MarketValue, 'HostValue'),
        'proposed_value': return_value_or_none(collateral.MarketValue, 'HostValue')
    }


    facility_limit = {
        'host_value': 0,
        'proposed_value': 0
    }

    outstanding_balance = {
        'host_value': 0,
        'proposed_value': 0
    }

    total_exposure = {
        'host_value': 0,
        'proposed_value': 0
    }


    coverages = Coverage.objects.filter(CollateralId=collateral_id)

    for coverage in coverages:
        if coverage.FacilityId is not None:
            facility = coverage.FacilityId

            lien_order = coverage.LienOrder
            assignment = coverage.Assignment
            if assignment is not None and lien_order is not None:
                facility_limit['host_value'] = (facility_limit.get('host_value') + (return_value_or_none(facility.CommitmentValue, 'HostValue') * assignment) if return_value_or_none(facility.CommitmentValue, 'HostValue') is not None and isinstance(return_value_or_none(facility.CommitmentValue, 'HostValue'), float or int) else 0)
                facility_limit['proposed_value'] = (facility_limit.get('proposed_value') + (return_value_or_none(facility.CommitmentValue, 'ProposedValue') * assignment) if return_value_or_none(facility.CommitmentValue, 'ProposedValue') is not None and isinstance(return_value_or_none(facility.CommitmentValue, 'ProposedValue'), float or int) else 0)

                outstanding_balance['host_value'] = (outstanding_balance.get('host_value') + (return_value_or_none(facility.BalanceValue, 'HostValue') * assignment) if return_value_or_none(facility.BalanceValue, 'HostValue') is not None and isinstance(return_value_or_none(facility.BalanceValue, 'HostValue'), float or int) else 0)
                outstanding_balance['proposed_value'] = (outstanding_balance.get('proposed_value') + (return_value_or_none(facility.BalanceValue, 'ProposedValue') * assignment) if return_value_or_none(facility.BalanceValue, 'ProposedValue') is not None and isinstance(return_value_or_none(facility.BalanceValue, 'ProposedValue'), float or int) else 0)

                total_exposure['host_value'] = (total_exposure.get('host_value') + (return_value_or_none(facility.ExposureTotal, 'HostValue') * assignment) if return_value_or_none(facility.ExposureTotal, 'HostValue') is not None and isinstance(return_value_or_none(facility.ExposureTotal, 'HostValue'), float or int) else 0)
                total_exposure['proposed_value'] = (total_exposure.get('proposed_value') +  (return_value_or_none(facility.ExposureTotal, 'ProposedValue') * assignment) if return_value_or_none(facility.ExposureTotal, 'ProposedValue') is not None and isinstance(return_value_or_none(facility.ExposureTotal, 'ProposedValue'), float or int) else 0)

    utilization_by_omv = {
        'host_value': (total_exposure.get('host_value') / open_market_value.get('host_value')) if open_market_value.get('host_value') is not None and total_exposure.get('host_value') != 0 else None,
        'proposed_value': (total_exposure.get('proposed_value') / open_market_value.get('proposed_value')) if open_market_value.get('proposed_value') is not None and total_exposure.get('proposed_value') != 0 else None
    }
    utilization_by_dv = {
        'host_value': (total_exposure.get('host_value') / discounted_value.get('host_value')) if discounted_value.get('host_value') is not None and total_exposure.get('host_value') != 0 else None,
        'proposed_value': (total_exposure.get('proposed_value') / discounted_value.get('proposed_value')) if discounted_value.get('proposed_value') is not None and total_exposure.get('proposed_value') != 0 else None
    }
    utilization_by_fsv = {
        'host_value': (total_exposure.get('host_value') / forced_sale_value.get('host_value')) if forced_sale_value.get('host_value') is not None and total_exposure.get('host_value') != 0 else None,
        'proposed_value': (total_exposure.get('proposed_value') / forced_sale_value.get('proposed_value')) if forced_sale_value.get('proposed_value') is not None and total_exposure.get('proposed_value') != 0 else None
    }

    return [
        {'parameterGroup': 'Exposure Info', 'parameter': 'Facility Limit', 'facility': True, 'hostValue': facility_limit.get('host_value', None), 'proposedValue': facility_limit.get('proposed_value', None)},
        {'parameterGroup': 'Exposure Info', 'parameter': 'Outstanding Balance', 'facility': True, 'hostValue': outstanding_balance.get('host_value', None), 'proposedValue': outstanding_balance.get('proposed_value', None)},
        {'parameterGroup': 'Exposure Info', 'parameter': 'Total Exposure', 'facility': True, 'hostValue': total_exposure.get('host_value', None), 'proposedValue': total_exposure.get('proposed_value', None)},
        {'parameterGroup': 'Collateral Info', 'parameter': 'Open Market Value (OMV)', 'collateral': True, 'hostValue': open_market_value.get('host_value', None), 'proposedValue': open_market_value.get('proposed_value', None)},
        {'parameterGroup': 'Collateral Info', 'parameter': 'Discounted Value (DV)', 'collateral': True, 'hostValue': discounted_value.get('host_value', None), 'proposedValue': discounted_value.get('proposed_value', None)},
        {'parameterGroup': 'Collateral Info', 'parameter': 'Forced Sale Value (FSV)', 'collateral': True, 'hostValue': forced_sale_value.get('host_value', None), 'proposedValue': forced_sale_value.get('proposed_value', None)},
        {'parameterGroup': 'Coverage Ratios', 'parameter': 'Coverage By OMV', 'collateral': True, 'hostValue': utilization_by_omv.get('host_value', None), 'proposedValue': utilization_by_omv.get('proposed_value', None)},
        {'parameterGroup': 'Coverage Ratios', 'parameter': 'Coverage By DV', 'collateral': True, 'hostValue': utilization_by_dv.get('host_value', None), 'proposedValue': utilization_by_dv.get('proposed_value', None)},
        {'parameterGroup': 'Coverage Ratios', 'parameter': 'Coverage By FSV', 'collateral': True, 'hostValue': utilization_by_fsv.get('host_value', None), 'proposedValue': utilization_by_fsv.get('proposed_value', None)}
    ]