import sys
import ast

def calculate_tax(tax_boundaries,tax_percent, income):
    tax = 0
    if income > tax_boundaries[0]:
        fulltaxed=[0]
        for index in range(0,3):
            fulltaxed.append((tax_boundaries[index+1]-tax_boundaries[index])*tax_percent[index])

        for index in range(3,0,-1):
            re = income-tax_boundaries[index]
            if re >= 0:
                tax= re*tax_percent[index]+sum(fulltaxed[0:index+1])
                break
    return tax

def calculate_insurance(insurance_rate_employee,insurance_rate_employer,exemption_income,taxeable_income):
    income_insurance_rate_employee=0.0
    income_insurance_rate_employer=0.0
    if taxeable_income > exemption_income:
        income_insurance_rate_employee = insurance_rate_employee * taxeable_income
        income_insurance_rate_employer = insurance_rate_employer * taxeable_income
    return [round(income_insurance_rate_employee,2),round(income_insurance_rate_employer,2)]

def check_arguments(): # pragma: no cover
    if sys.argv.__len__() > 1:
        if sys.argv[1].__contains__("-h") or sys.argv[1].__contains__("--help"):
            print("You need to provide input argument as bellow \n \
                1: your income (mountly), this is the MANDATORY argumant \n \
                2: Taxeable income (mountly) \n \
                3: exemption for insurance tax (mountly) \n \
                4: a list indicates the tax boundaries in tomans such as [10000000,14000000,23000000,34000000] which is the default rates for year 1402 in Iran. (Optional) \n \
                5: a list indicates the tax percentages such as [0.10,0.15,0.20,0.30] which is the default rates for year 1402 in Iran. (Optional)")
            exit()
    else:
        print("You need to provide input argument, type -h or --help for help")
        exit(1)

def without_test():
    return "Hi there"


def main(): # pragma: no cover
    insurance_rate_employee = 0.07
    insurance_rate_employer = 0.23
    income=18000000
    tax_boundaries=[10000000,14000000,23000000,34000000]
    tax_percent=[0.10,0.15,0.20,0.30]
    exemption_income= 176943 * 30

    check_arguments()
    if sys.argv[1] is not None and sys.argv[1].isdigit():
        income = float(sys.argv[1])
        taxeable_income=income
    else:
        print("You need to provide your income (mountly), this is the mandatory argumant")
        exit(1)
    if sys.argv.__len__() > 2 and sys.argv[2] is not None:
        taxeable_income = ast.literal_eval(sys.argv[2])
    if sys.argv.__len__() > 3 and sys.argv[3] is not None:
        exemption_income = ast.literal_eval(sys.argv[3])
    if sys.argv.__len__() > 4 and sys.argv[4] is not None:
        tax_boundaries = ast.literal_eval(sys.argv[4])
    if sys.argv.__len__() > 5 and sys.argv[5] is not None:
        tax_percent = ast.literal_eval(sys.argv[5])
    

    income_insurance_rate_employee,income_insurance_rate_employer = calculate_insurance(insurance_rate_employee,insurance_rate_employer,exemption_income,taxeable_income)
    tax = calculate_tax(tax_boundaries,tax_percent, income)
    net_income = income-tax-income_insurance_rate_employee

    print(f'You should pay {tax:.2f} in tax for {income} income! the insurance tax is {income_insurance_rate_employee+income_insurance_rate_employer:.2f}, there is a subtle differences for 31-day and 30-day mounts.')
    print(f'You should pay {income_insurance_rate_employee:.2f} and your company pays {income_insurance_rate_employer:.2f} of insurance tax.')
    print(f'Sum of deduction on your income is {tax+income_insurance_rate_employee:.2f}.')
    print(f'The net income is {net_income:.2f}.')

    without_test()

if __name__ == "__main__":
    main() # pragma: no cover

