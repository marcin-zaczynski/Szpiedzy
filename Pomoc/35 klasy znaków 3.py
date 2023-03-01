import re

wynik = re.match(r'^((?:He)(?P<pierwsza>ll)o) (World)+(!|\.)$', 'Hello World.')

if wynik:
    print('Dopasowano!')
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    print(wynik.group(2))
    print(wynik.group(3))
    print(wynik.groups())
    print(wynik.group('pierwsza'))
else:
    print('Nie dopasowano!')
email = 'mavix@op.pl'
if re.match(r'^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9\.-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9-\.]+[A-Za-z0-9])\.[A-Za-z0-9]++$', email):
    print('Dopasowano!')

else:
    print('Nie dopasowano!')

