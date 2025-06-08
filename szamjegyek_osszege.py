'''
A program bekér egy számot, majd összeadja a számjegyeit.
Ha a felhasználó nem szeretne több számot megadni, üssön ENTER-t.
'''
print('A kilépéshez üssön ENTER-t')

while (szam := (input('Kérek egy számot!  '))) != '':
    osszeg = 0
    for jegy in szam:
        osszeg += int(jegy)
    print(f'A számjegyek összege:  {osszeg}')