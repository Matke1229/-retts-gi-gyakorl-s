tokeletesek = []

while (szam := (input('Kérek egy számot!  '))) != '':
    osztok = []
    for i in range(1, int(szam)):
        if int(szam) % i == 0:
            osztok.append(i)
    osszeg = 0
    for oszto in osztok:
        osszeg += oszto
    if osszeg == int(szam):
        print('A megadott szam tökéletes szám.')
        tokeletesek.append(szam)
    else:
        print('A megadott szám nem tökéletes.')
print('A megadott számok közül tökéletesek voltak:')
print(', '.join(tokeletesek))