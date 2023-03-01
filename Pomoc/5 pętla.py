i = 0


while i <5 :    # while pętla słowo do póki
    print(i)
    i += 1
print('Koniec')

while True:
    print(i)
    i +=1
    if i >=10:
        break    #przerwij, złam
print('koniec 2')

while True:
    i +=1
    if i % 2 == 1:
        continue   #kontynuuj
    print(i)
    if i >=15:
        break    #przerwij, złam
print('koniec 3')