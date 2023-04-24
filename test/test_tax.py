import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from main import calculate_tax
from main import calculate_insurance

@pytest.mark.parametrize("income, expected_tax",[
    (9000000,0),
    (0,0),
    (-1,0),
    (23000000,1750000),
    (18000000,1000000),
    (28000000,2750000),
    (28000000000,8393750000)
    ])
def test_calculate_tax(income,expected_tax):
    
    tax_boundaries=[10000000,14000000,23000000,34000000]
    tax_percent=[0.10,0.15,0.20,0.30]
    
    assert calculate_tax(tax_boundaries, tax_percent, income) == expected_tax

@pytest.mark.parametrize("taxeable_income, expected_tax_employee,expected_tax_employer",[
    (5308270,0,0),
    (0,0,0),
    (-1,0,0),
    (33310172,2331712.04,7661339.56),
    (18000000,1260000.00,4140000.00),
    (28000000,1960000.00,6440000.00)
    ])
def test_calculate_insurance(taxeable_income,expected_tax_employee,expected_tax_employer):
    
    insurance_rate_employee = 0.07
    insurance_rate_employer = 0.23
    exemption_income= 176943 * 30
    
    assert calculate_insurance(insurance_rate_employee,insurance_rate_employer,exemption_income,taxeable_income) == [expected_tax_employee,expected_tax_employer]