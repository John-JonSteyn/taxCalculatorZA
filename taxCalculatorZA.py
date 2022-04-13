"""
    Range                   | rate
1|  1 – 226 000             | 18%
2|  226 001 – 353 100       | 26%
3|  353 101 – 488 700       | 31%
4|  488 701 – 641 400       | 36%
5|  641 401 – 817 600       | 39%
6|  817 601 – 1 731 600     | 41%
7|  1 731 601 and above     | 45%

Rebates:    | Age   | Amount
Primary     |       | 16 425
Secondary   | 65+   | 9 000
Tertiary    | 75+   | 2 997

"""
# Begin
for i in range(125):
    print('_', end = '')

print('\nCalculate your income tax for 2022 / 2023')
print('Use this income tax calculator to work out your monthly take-home pay')

age = int(input('\nPlease enter your age:\t\t\t\t'))

# Primary Rebate
rebate              = 16425
# Secondary Rebate
if 65 <= age:
    rebate          = rebate + 9000
# Tertiary Rebate
if 75 <= age:
    rebate          = rebate + 2997

timeFrame   = str.upper(input('\nHow ofthen do you get paid?\nPlease enter A for Annually or M for Monthly:\t'))

while (timeFrame != str('A')) and (timeFrame != str('M')):
    print(timeFrame)
    timeFrame   = str.upper(input('Your selection is invalid.\nPlease enter A for Annually or M for Monthly:\t'))


salaryBrutoY        = float(input('\nHow much do you earn before tax?\t\tZAR:'))
# Get Yearly
if  timeFrame   == str('M'):
    salaryBrutoY    = salaryBrutoY * 12
    incomeUntaxed   = salaryBrutoY
else:
    incomeUntaxed   = salaryBrutoY

taxY                = 0
taxBracket          = 'n/n'

# ZAR 1731601 +                 - 45%
if  incomeUntaxed  >= 1731601:
    bracketAmount   = incomeUntaxed - 1731601
    bracketTax      = bracketAmount * (45 / 100)
    taxY            = taxY + bracketTax
    incomeUntaxed   = incomeUntaxed - bracketAmount
    if taxBracket   == 'n/n':   taxBracket = '45'

# ZAR 817601 –  1731600         - 41%
if  incomeUntaxed  >= 817601:
    bracketAmount   = incomeUntaxed - 817601
    bracketTax      = bracketAmount * (41 / 100)
    taxY            = taxY + bracketTax
    incomeUntaxed   = incomeUntaxed - bracketAmount
    if taxBracket   == 'n/n':   taxBracket = '41'

# ZAR 641401 –  817600          - 39%
if  incomeUntaxed  >= 641401:
    bracketAmount   = incomeUntaxed - 641401
    bracketTax      = bracketAmount * (39 / 100)
    taxY            = taxY + bracketTax
    incomeUntaxed   = incomeUntaxed - bracketAmount
    if taxBracket   == 'n/n':   taxBracket = '39'

# ZAR 488701 –  641400          - 36%
if  incomeUntaxed  >= 488701:
    bracketAmount   = incomeUntaxed - 488701
    bracketTax      = bracketAmount * (36 / 100)
    taxY            = taxY + bracketTax
    incomeUntaxed   = incomeUntaxed - bracketAmount
    if taxBracket   == 'n/n':   taxBracket = '36'

# ZAR 353101 –  488700          - 31%
if  incomeUntaxed  >= 353101:
    bracketAmount   = incomeUntaxed - 353101
    bracketTax      = bracketAmount * (31 / 100)
    taxY            = taxY + bracketTax
    incomeUntaxed   = incomeUntaxed - bracketAmount
    if taxBracket   == 'n/n':   taxBracket = '31'

# ZAR 226001 –  353100          - 26%
if  incomeUntaxed  >= 226001:
    bracketAmount   = incomeUntaxed - 226001
    bracketTax      = bracketAmount * (26 / 100)
    taxY            = taxY + bracketTax
    incomeUntaxed   = incomeUntaxed - bracketAmount
    if taxBracket   == 'n/n':   taxBracket = '26'

# ZAR 1 –       226 000          - 18%
if  incomeUntaxed  >= 1:
    bracketAmount   = incomeUntaxed - 1
    bracketTax      = bracketAmount * (18 / 100)
    taxY            = taxY + bracketTax
    incomeUntaxed   = incomeUntaxed - bracketAmount
    if taxBracket   == 'n/n':   taxBracket = '18'

# Rebates
taxY        = taxY - rebate

# Income tax connot be negative
if taxY < 0:
    taxY    = 0

salaryBrutoM        = salaryBrutoY  / 12
taxM                = taxY          / 12
salaryNetY          = salaryBrutoY - taxY
salaryNetM          = salaryBrutoM - taxM
taxPerc             = (taxY  / salaryBrutoY) * 100

# Annual
print('\nYour yearly income before tax is\t\tZAR{0:.2f}'.format(salaryBrutoY))
print('Your yearly income tax\t\t\t\tZAR{0:.2f}'.format(taxY))
print('Your net income after tax is\t\t\tZAR{0:.2f} yearly'.format(salaryNetY))

# Montly
print('\nYour monthly income before tax is\t\tZAR{0:.2f}'.format(salaryBrutoM))
print('Your mothly income tax is\t\t\tZAR{0:.2f}'.format(taxM))
print('Your net monthly income after tax is\t\tZAR{0:.2f} monthly'.format(salaryNetM))

# Percentage
print('\nYour tax bracket:\t\t\t\t{}%'.format(taxBracket))
print('The tax you pay is equal to:\t\t\t{0:.2f}%'.format(taxPerc))

# Disclaimer
print('\nNote: Results do not cater for all scenarios and should be used as an indicator only.')
print('Based on SARS\' tax pocket guide provides a synopsis of the most important tax, duty and levy related information for 2022/23')
print('For more information please visit https://github.com/Bearded-Viking/TaxCalCulatorZA')

# End
for i in range(125):
    print('_', end = '')