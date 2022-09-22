from Tema3.my_package_hw3.my_variables_hw_three import n, verificare, pal, prim, divizori, divizor_mare


def f1(n):
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

    if a == str(a)[::-1]:
        print('Numarul este palindrom')
        pal = True
    else:
        print('Numarul nu este palindrom')
        pal = False
    if a > 1:
        for i in range(2, int(a / 2) + 1):
            if (a % i) == 0:
                print('Numarul nu este prim')
                prim = False
            break
    else:
        print('Numarul este prim')
        prim = True
    if a >= 0:
        for i in range(2, a // 2 + 1):
            if a % i == 0:
                divizori.append(i)
    if a >= 0:
        for i in range(2, a):
            if a % i == 0:
                divizor_mare = i
        cifre = len(str(a))

    operatii_numar = {
            "is_palindrome": pal,
            "divisors": divizori,
            "is_prime": prim,
            "max_divisor": divizor_mare,
            "digits": cifre,
        }
    print(operatii_numar)


