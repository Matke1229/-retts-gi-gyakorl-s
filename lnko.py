'''
A program megadja két a felhasználó által megadott szám legnagyobb közös osztóját.
A program egész számokkal dolgozik. (oszthatóság)
Egyszerre két számot kell megadni, ha a felhasználó nem akar több számpárt megadni, üssön ENTER-t.
'''

while (szam_1 := (input('Kérek egy számot!  '))) != '':
    szam_2 = int(input('Kérem a másik számot!  '))
    kisebb = int(szam_1)
    if int(szam_1) > szam_2:
        kisebb = szam_2
    lnko = 1
    for i in range(kisebb):
        i += 1
        if int(szam_1) % i == 0 and szam_2 % i == 0:
            lnko = i
    print(f'A két szám legnagyobb közös osztója: {lnko}')  