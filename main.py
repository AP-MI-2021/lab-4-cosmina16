import math
from math import trunc , sqrt

def citire_lista():
    result_list = []
    dimensiune = int(input("Dimensiune lista "))
    while dimensiune:
        element = float(input('introduceti un element'))
        result_list.append(element)
        dimensiune -=1
    return result_list



def numere_intregi(n):
    """
    verifica daca un numar n este intreg sau nu
    :param n:un numar
    :return: true daca numarul este intreg ,false in caz contrar
    """
    if n == int(n):
        return True
    else:
        return False

def test_numere_intregi():
    assert numere_intregi(2.0) == True
    assert numere_intregi(3.2) == False

def all_nr_intregi(lista):
    rez = []
    for i in lista:
        if numere_intregi(i):
            rez.append(i)
    return rez



def celmaimarenr_div_cu_n(lista,n):
    """
    determina celmai mare nr div cu n din lista
    :param lista: lista de nr
    :param n: un numar citit de la tastatura
    :return: cel mai mare numar din lista div cu n
    """
    b=1
    for i in lista:
        if i%n==0 and b==1:
            b=0
            max=i
        elif i%n==0 and i>max:
            max=i
    return max



def verif_partefrac(n):
    """
    returneaza parte frac a unui nr
    :param n: un nr float
    :return: partea fractionara
    """
    return str(n).split('.')[1]

def test_verif_partefrac():
    assert verif_partefrac(3.323) == '323'
    assert verif_partefrac(3.56) == '56'

def numar_palindrom(n):
    """
    verifica daca n e palindrom
    :param n: un numar natural
    :return: true daca e palindrom ,false in caz contrar
    """
    m=n
    inv =0
    while m> 0:
      inv=inv*10+m%10
      m//=10
    return inv==n

def test_numar_palindrom():
    assert test_numar_palindrom(33) == True
    assert test_numar_palindrom(34) == False

def nr_parte_frac_pal(lista):
    rez =[]
    for i in lista:
        if numar_palindrom(int(verif_partefrac(i))):
            rez.append(i)
    return rez

def test_nr_parte_frac_pal():
    assert nr_parte_frac_pal([2.121 , 3.89 , 0.78, 9.898])==[2.121, 9.898]



def is_prime(numar):
    """
    verifica daca numarul e prim sau nu
    :param numar: un numar
    :return: true daca e prim false in caz contrar
    """
    if numar < 2:
        return False
    if numar == 2:
        return True
    if numar % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(numar)) + 1, 2):
        if numar % x == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(13) == True
    assert is_prime(12) == False

def my_function(x):
    """
    treansforma un nr in strig si il intoarce
    :param x: un nr
    :return: un string invers fata de nr
    """
    x= str(x)
    return x[::-1]

def transf_lista(lista):
    list = []
    for i in lista:
        if is_prime(trunc(sqrt(i))):
            list.append(my_function(i))
        else:
            list.append(i)
    return list



def main():
    stop = False
    lista = []
    while not stop:
        print ("""
        1 Citire lista 
        2 afisare numere intregi
        3 afiseaza cel mai mare numar div cu n din lista
        4 afiseaza numere cu partea fractionara palindrom
        5 transforma sirul (prim(trunc(sqrt(x))) adev =>...face rev)
        x Exit
        """)
        command = input("alege comanda ")
        if command == 'x':
            stop = True
        elif command == '1':
            lista = citire_lista()
        elif command == '2':
            test_numere_intregi()
            lista_numere_intregi = all_nr_intregi(lista)
            print(lista_numere_intregi)
        elif command == '3':
            n = int(input("Dati un nr "))
            print(celmaimarenr_div_cu_n(lista,n))
        elif command == '4':
            test_verif_partefrac()
            test_numar_palindrom()
            test_nr_parte_frac_pal()
            lista_palindrom =nr_parte_frac_pal(lista)
            print(lista_palindrom)
        elif command == '5':
            test_is_prime()
            print(transf_lista(lista))


if __name__ == "__main__":
    main()

