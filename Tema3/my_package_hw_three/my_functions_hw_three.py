from Tema3.my_package_hw_three.my_variables_hw_three import n, pal, prim, divizori, divizor_mare


def f1():
    a = input('Introduceti un numar intreg de la tastatura:')
    try:
        a = int(a)
    except ValueError:
        print('')
    finally:
        if type(a) is not int:
            verificare = False
            while verificare == False:
                a = input('Introduceti un numar intreg sau iesiti tastand \"exit\" sau \"quit\": \n>')
                try:
                    a = int(a)
                except ValueError:
                    print('')
                if a == 'quit' or a == 'exit':
                    return 0
                if type(a) is int:
                    break
        if type(a) is int:
            print('Ati introdus numarul intreg', a)
            return a

def f_palindrom():
    if a == str(a)[::-1]:
        print('Numarul este palindrom')
        return pal == True
    else:
        print('Numarul nu este palindrom')
        return pal == False

def f_prim():
    for i in range(2, int(a / 2) + 1):
        if (a % i) == 0:
            print('Numarul nu este prim')
            prim = False
            return prim
        break
    else:
        print('Numarul este prim')
        prim = True
        return prim

def f_divizori():
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            divizori.append(i)
            return divizori

def f_divizor_mare():
    for i in range(2, a):
        if a % i == 0:
            divizor_mare = i
            return divizor_mare

def f_cifre():
    if a >= 0:
        cifre = len(str(a))
        return cifre

def f_operatii():
    operatii_numar = {
        "is_palindrome": pal,
        "divisors": divizori,
        "is_prime": prim,
        "max_divisor": divizor_mare,
        "digits": len(str(a)),
    }
    print(operatii_numar)
