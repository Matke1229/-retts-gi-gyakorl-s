while (szo := (input('Az egész programból való kilépéshez írja be a kilép szót, a folytatáshoz pedig a folytat szót. '))).upper() != 'KILÉP':
    if szo.upper() == 'FOLYTAT':
        szamok = []
        while (szam := (input('Kérek egy számot!  '))) != '':
            szamok.append(szam)
        szamok_1 = []
        for szam in szamok:
            if szam not in szamok_1:
                szamok_1.append(szam)
        gyakorisag = []
        for i in range(len(szamok_1)):
            db = 0
            lista = []
            lista.append(szamok_1[i])
            for szam in szamok:
                if szamok_1[i] == szam:
                    db += 1
            lista.append(str(db))
            gyakorisag.append(lista)
        for i in range(len(szamok_1)):
            legtobb = 0
            for szam in gyakorisag:
                if int(szam[1]) > int(legtobb):
                    legtobb = szam[1]
                    a_szam = szam[0]
            ami_kell = []
            ami_kell.append(a_szam)
            ami_kell.append(str(legtobb))
            print(', '.join(ami_kell), end=' ')
            print('db')
            gyakorisag.remove(ami_kell)