import sys
import ast

insurance_rate_employee = 0.07
insurance_rate_employer = 0.3
income=10000000
tax_boundaries=[10000000,14000000,23000000,34000000]
tax_percent=[0.10,0.15,0.20,0.30]

if sys.argv.__len__() > 1:
    if sys.argv[1].__contains__("-h") or sys.argv[1].__contains__("--help"):
        print("You need to provide input argument as bellow \n \
            1: your income (mountly), this is the MANDATORY argumant \n \
            2: a list indicates the tax boundaries in tomans such as [10000000,14000000,23000000,34000000] which is the default rates for year 1402 in Iran. (Optional) \n \
            3: a list indicates the tax percentages such as [0.10,0.15,0.20,0.30] which is the default rates for year 1402 in Iran. (Optional)")
        exit()    
    if sys.argv[1] is not None and sys.argv[1].isdigit():
        income = float(sys.argv[1])
    else:
        print("You need to provide your income (mountly), this is the mandatory argumant")
        exit(1)
    if sys.argv.__len__() > 2 and sys.argv[2] is not None:
        tax_boundaries = ast.literal_eval(sys.argv[2])
    if sys.argv.__len__() > 3 and sys.argv[3] is not None:
        tax_percent = ast.literal_eval(sys.argv[3])
else:
    print("You need to provide input argument, type -h or --help for help")
    exit(1)

fulltaxed=[0]
for index in range(0,3):
    fulltaxed.append((tax_boundaries[index+1]-tax_boundaries[index])*tax_percent[index])

for index in range(3,0,-1):
    re = income-tax_boundaries[index]
    if re >= 0:
        tax= re*tax_percent[index]+sum(fulltaxed[0:index+1])
        break

income_insurance_rate_employee = income * insurance_rate_employee
income_insurance_rate_employer = income * insurance_rate_employer

print("You should pay {:.2f} tax for {} income! the insurance tax is {:.2f} that you should pay {:.2f} of it, so sum of deduction on your income is {:.2f} and the net income is {:.2f}".format(tax,income,income_insurance_rate_employer,income_insurance_rate_employee,tax+income_insurance_rate_employee,income-tax-income_insurance_rate_employee))