from Tema3.my_package_hw3.my_variables_hw3 import a, n, vef


def f1(a, n, vef):
    try:
        a = int(a)
    except ValueError:
        print('Introduceti un numar intreg sau iesiti tastand \"exit\" sau \"quit\".')
    finally:
        if type(a) is not int:
            vef == False
            while vef == False:
                print('Introduceti un numar intreg sau iesiti tastand \"exit\" sau \"quit\".')
                if a == 'quit' or a == 'exit':
                    return 0
        if type(a) is int:
            print('Ati introdus numarul intreg', a)
            n += 1
        if n == 1:
            print('Numarul 20 este par')
