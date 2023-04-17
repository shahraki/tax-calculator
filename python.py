import sys
# import time
# a=8
# print(a+9)
# add = lambda x, y: x + y
# print(add(3,4))
# while True:
#     time.sleep(10)

import numpy as np
base=1000000
income=10000000
tax_boundaries=base*np.array([10,14,23,34])
tax_percent=[0.10,0.15,0.20,0.30]

if sys.argv.__len__() > 0:
    if sys.argv[0].__contains__("-h") or sys.argv[0].__contains__("--help"):
        print("You need to provide input argument as bellow \
            1: your income (mountly), this is the mandatory argumant\
            2: a list indicates the tax boundaries in tomans such as [10000000,14000000,23000000,34000000] which is the default rates for year 1402 in Iran. (Optional)\
            3: a list indicates the tax percentages such as [0.10,0.15,0.20,0.30] which is the default rates for year 1402 in Iran. (Optional)"    )
    if sys.argv[0] is not None and sys.argv[0].isdigit():
        income = sys.argv[0]
    else:
        print("You need to provide your income (mountly), this is the mandatory argumant")
        exit(1)

    if sys.argv[1] is not None and isinstance(sys.argv[1], list):
        tax_boundaries=sys.argv[1]
    if sys.argv[2] is not None and isinstance(sys.argv[2], list):
        tax_percent=sys.argv[1]

fulltaxed=[0]

for index in range(0,3):
    fulltaxed.append((tax_boundaries[index+1]-tax_boundaries[index])*tax_percent[index])

for index in range(3,0,-1):
    re = income-tax_boundaries[index]
    if re > 0:
        tax= re*tax_percent[index]+sum(fulltaxed[0:index+1])
        break

print("You should pay {} tax for {} income!".format(tax,income))