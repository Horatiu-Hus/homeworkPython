def my_function(*args, **kwargs):
    suma = 0
    if type(kwargs) == float:
        suma += args
    for x in args:
        if type(x) == int or type(x) == float:
            suma += x
    else:
        return suma


print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', args=2))


def my_sum(n):
    if n == 0:
        return 0
    return n + my_sum(n - 1)

sum_ = my_sum(99)
print('sum', sum_)


def my_sum_even(n):
    if n == 0:
        return 0
    if not n % 2 == 0:
        return my_sum_even(n - 1)
    else:
        return n + my_sum_even(n - 2)

print(my_sum_even(11))


def my_sum_odd(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return my_sum_odd(n - 1)
    else:
        return n + my_sum_odd(n - 1)

print(my_sum_odd(10))


a = int(input('Introduceti un numar intreg = '))

def my_function_number(x):
    if type(a) == int:
        print('Numarul citit este:', a)
    else:
        print('Numarul introdus nu este un numar intreg!')
        return 0


my_function_number(0)



