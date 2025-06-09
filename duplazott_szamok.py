'''
A program számokat kér be a felhasználótól, amíg ENTER-t nem üt.
A számokat eltárolásra kerülnek egy listában.
A végén kiírásra kerülnek azok a számok, amik töbször fordultak elő és ezek száma.
Az egész programból való kilépéshez írja be a kilép szót.
'''
while (szo := (input('Az egész programból való kilépéshez írja be a kilép szót, a folytatáshoz pedig a folytat szót. '))).upper() != 'KILÉP':
    if szo.upper() == 'FOLYTAT':
        szamok = []
        while (szam := (input('Kérek egy számot!  '))) != '':
            szamok.append(szam)
        szamok_1 = []
        szamok_2 = []
        for szam in szamok:
            if szam not in szamok_1:
                szamok_1.append(szam)
            elif szam in szamok_1 and szam not in szamok_2:
                szamok_2.append(szam)
        print(f'{len(szamok_2)} db szám van, ami többször előfordul és ezek:')
        print(', '.join(szamok_2))