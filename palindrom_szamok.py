'''
A program bekér számokat és eldönti, hogy palindrom-e vagy sem.
Ha több palindrom számot ad meg a felhasználó, akkor azokat összegyüjti egy listában és a végén kiírja azokat.
Ha a felhasználó nem szeretne több számot megadni, nyomjon ENTER-t.
'''

print('A kilépéshez üssön ENTER-t')

palindromok = []
while (szam := (input('Kérek egy számot!  '))) != '':
    szamjegyek = []
    for szamjegy in szam:
        szamjegyek.append(szamjegy)
    index = -1
    visszafele = ''
    for i in range(len(szamjegyek)):
        visszafele += szamjegyek[index]
        index -= 1
    if szam == visszafele:
        print('A megadott szám palindrom')
        palindromok.append(szam)
    else:
        print('A megadott szám nem palindrom')
        
if len(palindromok) > 1:
    print(', '.join(palindromok))
    