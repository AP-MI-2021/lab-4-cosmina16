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




#5





def main():
    lista = []
    while True:
        print("1.Citire date")
        print("2.Afisaza partea intreaga din fiecare numar")
        print("3. ")
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
            pass
        elif optiune == '5':
            pass
        elif optiune == 'x':
            break
        else:
            print("Optiune gresita")

if __name__ == '__main__':
    main()