def f1():
    global a
    a = input('Introduceti un numar intreg!\n>')
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
    global a
    a = int(a)
    if str(a) == str(a)[::-1]:
        pal = True
        return pal
    pal = False
    return pal

def f_prim():
    global a
    a = int(a)
    for i in range(2, a):
        if (a % i) == 0:
            prim = False
            return prim
    else:
        prim = True
        return prim

def f_divizori():
    global a
    a = int(a)
    divizori = []
    for i in range(2, a):
        if a % i == 0:
            divizori.append(i)
    return divizori

def f_divizor_mare():
    global a
    a = int(a)
    for i in range(2, a):
        if a % i == 0:
            divizor_mare = i
    return divizor_mare


def f_operatii(pal, divizori, prim, divizor_mare):
    operatii_numar = {
        "is_palindrome": pal,
        "divisors": divizori,
        "is_prime": prim,
        "max_divisor": divizor_mare,
        "digits": len(str(a)),
    }
    print(operatii_numar)
