import re

if re.match('^[A-Z][a-z]*$','Marcin'):

    print('Dopasowano')
else:
    print('Nie dopasowano')

if re.match('^[A-Z][a-z]+$','Marcin'):

    print('Dopasowano!')
else:
    print('Nie dopasowano!')

if re.match('^[A-Z][a-z]?[A-Z]$','AdA'):

    print('Dopasowano')
else:
    print('Nie dopasowano')

if re.match('^[A-Z][a-z]{2,5}$','Marcinn'):

    print('Dopasowano')
else:
    print('Nie dopasowano')

