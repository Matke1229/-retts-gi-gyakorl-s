'''
A program bekér egy mondatot, majd megszámolja hány magánhangzót tartalmaz és ezeket ki is írja.
A program addig fut, amíg a felhasználó nem csak ENTER-t üt.
'''

magan = ['a', 'á', 'e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű', 'u', 'ú', 'o', 'ó']
while(mondat := (input('Kérek egy mondatot!  '))) != '':
    db = 0
    jo_magan = []
    for betu in mondat:
        if betu.lower() in magan:
            db += 1
            if betu.lower() not in jo_magan and betu.upper() not in jo_magan:
                jo_magan.append(betu)
    print('Magánhangzók:', end=' ')
    print(', '.join(jo_magan))
    print(f'{db}db magánhangzó szerepel a megadott szóban.')