#1
def citire_lista():
    lista = []
    dimensiune = int(input("Dimensiune lista "))
    while dimensiune:
        element = float(input('introduceti un element'))
        lista.append(element)
        dimensiune -=1
    return lista


#2
def afis_partint(lista):
    """
    returneaza o lista doar din partile intregi
    :param lista: o lista cu numere float
    :return: o  lista doar din numere intregi
    """

    rez = []
    for i in lista:
        rez.append(int(i))
    return rez

def test_afis_partint():
    assert afis_partint([1.5, -3.3, 8, 9.8, 3.2]) == ([1, -3, 8, 9, 3])


#3
def interval_deschis(lista,capat1,capat2):
    """
    returneaza o lista care contine elemente care apartin unui interval
    :param lista: cu numere float
    :param capat1: capatul inferior
    :param capat2: capatul superior
    :return:
    """
    rez = []
    for i in lista:
        if i>capat1 and i< capat2:
            rez.append(i)
    return rez

def test_interval_deschis():
    assert interval_deschis([1.5, -3.3, 8, 9.8, 3.2] , -4 , 5) == ([1.5, -3.3, 3.2])

#4
def parte_frac(n):
    """
    returneaza partea fractionara a unui numar
    :param n: un numar float
    :return: partea frac a unui numar
    """
    return str(n).split('.')[1]


def partfrac_partint(lista):
    """
    returneaza o lista care contine doar numerele a caror parte intreaga este divizor al partii fractionare
    :param lista: o lista de numere float
    :return: elementele care au partea intreaga divizor al partii fractionare
    """
    rez = []
    for i in lista:
        n = int(parte_frac(i))
        z = int(i)
        if n%z==0 and z!= 0:
            rez.append(i)
    return rez




#5
def transformare(lista):
    """
    returneaza
    :param lista:
    :return:
    """
    rez = []
    p ='\0'
    for i in lista:
        n= str(i)
        for j in n:
            if j== '-':
                p=p+"minus"
            elif j== '0':
                p=p+"zero"
            elif j == '1':
                p = p + "unu"
            elif j == '2':
                p = p + "doi"
            elif j == '3':
                p = p + "trei"
            elif j == '4':
                p = p + "patru"
            elif j == '5':
                p = p + "cinci"
            elif j == '6':
                p = p + "sase"
            elif j == '7':
                p = p + "sapte"
            elif j == '8':
                p = p + "opt"
            elif j == '9':
                p = p + "noua"
            else:
                j== '.'
                p= p+ "virgula"
        rez.append(p)
        p='\0'
    return rez







def main():
    lista = []
    while True:
        print("1.Citire date")
        print("2.Afisaza partea intreaga din fiecare numar")
        print("3.Afiseaza elementele care apartin unui interval deschis")
        print("4.Afiseaza elementele care care au partea intreaga divizor al partii fractionare ")
        print("5.Transformarea in stringuri a numerelor")
        print("x. Iesire")
        optiune = input(" Dati optiunea: ")
        if optiune == '1':
            lista = citire_lista()
        elif optiune == '2':
            test_afis_partint()
            rez = []
            rez = afis_partint(lista)
            print (rez)
        elif optiune == '3':
            test_interval_deschis()
            capat1 = float(input(" capatul inferior"))
            capat2 = float(input(" capatul superior"))
            rez = []
            rez =interval_deschis(lista,capat1,capat2)
            print(rez)
        elif optiune == '4':
            rez = []
            rez = partfrac_partint(lista)
            print(rez)
        elif optiune == '5':
            rez = []
            rez = transformare(lista)
            print(rez)
        elif optiune == 'x':
            break
        else:
            print("Optiune gresita")

if __name__ == '__main__':
    main()