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





def main():
    lista = []
    while True:
        print("1.Citire date")
        print("2.Afisaza partea intreaga din fiecare numar")
        print("3.Afiseaza elementele care apartin unui interval deschis")
        print("4.Afiseaza elementele care care au partea intreaga divizor al partii fractionare ")
        print("5.")
        print("x. Iesire")
        optiune = input(" Dati optiunea: ")
        if optiune == '1':
            lista = citire_lista()
        elif optiune == '2':
            rez = []
            rez = afis_partint(lista)
            print (rez)
        elif optiune == '3':
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
            pass
        elif optiune == 'x':
            break
        else:
            print("Optiune gresita")

if __name__ == '__main__':
    main()