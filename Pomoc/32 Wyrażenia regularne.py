import re

wzor = r'banan'  # r przed string ignoruje znaki specjalne

tekst = r'gruszkabananjabłko'


if re.match(wzor, tekst): # match tylko na początku
    print('Dopasowano!')
else:
    print('Nie dopasowano!')

if re.search(wzor, tekst):  # search szuka w dowolnym miejscu
    print('Dopasowano!')
else:
    print('Nie dopasowano!')

print(re.findall(wzor, tekst)) # findall wyszukuje wszystkie wyszukania wzoru zwraca liste

dopasowanie = re.search(wzor, tekst)
if dopasowanie :
    print(dopasowanie.group())
    print(dopasowanie.start()) # początek dopasowania
    print(dopasowanie.end())   # koniec dopasowanie
    print(dopasowanie.span())  # początek i koniec krotka

tekst2 = re.sub(wzor, r'jagoda', tekst ) # modyfikuje i podmienia tekst
print(tekst2)