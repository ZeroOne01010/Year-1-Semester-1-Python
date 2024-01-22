#program to calculate total bill for number of minutes on a phone call

MINUTES_USED = int(input('Please enter the total number of minutes: '))
CALL_CHARGE = MINUTES_USED * 0.15
VAT = CALL_CHARGE * 0.2
TOTAL = CALL_CHARGE + VAT

print(
    f'Number of minutes used =: {MINUTES_USED}\nBasic call charge is: £ {CALL_CHARGE:.2f}\nVAT due is: £ {VAT:.2f}\nTotal bill is: £ {TOTAL:.2f}'
)



