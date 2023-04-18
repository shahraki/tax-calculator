import sys
import ast

def calculate_tax():
    fulltaxed=[0]
    for index in range(0,3):
        fulltaxed.append((tax_boundaries[index+1]-tax_boundaries[index])*tax_percent[index])

    for index in range(3,0,-1):
        re = income-tax_boundaries[index]
        if re >= 0:
            tax= re*tax_percent[index]+sum(fulltaxed[0:index+1])
            break

def calculate_insurance():
    income_insurance_rate_employee = insurance_rate_employee * taxeable_income
    income_insurance_rate_employer = insurance_rate_employer * taxeable_income

def main():
    insurance_rate_employee = 0.07
    insurance_rate_employer = 0.23
    income=18000000
    tax_boundaries=[10000000,14000000,23000000,34000000]
    tax_percent=[0.10,0.15,0.20,0.30]
    tax = 0
    if sys.argv.__len__() > 1:
        if sys.argv[1].__contains__("-h") or sys.argv[1].__contains__("--help"):
            print("You need to provide input argument as bellow \n \
                1: your income (mountly), this is the MANDATORY argumant \n \
                2: Taxeable income (mountly) \n \
                3: a list indicates the tax boundaries in tomans such as [10000000,14000000,23000000,34000000] which is the default rates for year 1402 in Iran. (Optional) \n \
                4: a list indicates the tax percentages such as [0.10,0.15,0.20,0.30] which is the default rates for year 1402 in Iran. (Optional)")
            exit()    
        if sys.argv[1] is not None and sys.argv[1].isdigit():
            income = float(sys.argv[1])
            taxeable_income=income
        else:
            print("You need to provide your income (mountly), this is the mandatory argumant")
            exit(1)
        if sys.argv.__len__() > 2 and sys.argv[2] is not None:
            taxeable_income = ast.literal_eval(sys.argv[2])
        if sys.argv.__len__() > 3 and sys.argv[3] is not None:
            tax_boundaries = ast.literal_eval(sys.argv[3])
        if sys.argv.__len__() > 4 and sys.argv[4] is not None:
            tax_percent = ast.literal_eval(sys.argv[4])
    else:
        print("You need to provide input argument, type -h or --help for help")
        exit(1)

    net_income = income-tax-income_insurance_rate_employee
    print(f'You should pay {tax:.2f} tax for {income} income! the insurance tax is {income_insurance_rate_employee+income_insurance_rate_employer:.2f}, there is a subtle difference for 31-day and 30-day mounts.')
    print(f'You should pay {income_insurance_rate_employee:.2f} and your company pays {income_insurance_rate_employer:.2f} of insurance tax.')
    print(f'Sum of deduction on your income is {tax+income_insurance_rate_employee:.2f}.')
    print(f'The net income is {net_income:.2f}.')