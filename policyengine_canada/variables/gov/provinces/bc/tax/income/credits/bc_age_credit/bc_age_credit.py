from policyengine_canada.model_api import *


class bc_age_credit(Variable):
    value_type = float
    entity = Person
    label = "British Columbia Age credit, non-refundable"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(
            period
        ).gov.provinces.bc.tax.income.credits.bc_age_credit
        eligible = age >= p.eligible_age
        income = person("total_individual_pre_tax_income", period)
        base = p.base
        reduction = p.phase_out.rate.calc(income)
        return eligible * (max_(0, base - reduction))
