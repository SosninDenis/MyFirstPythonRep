# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
# значение. При вызове функции должен создаваться объект-генератор. Функция вызывается
# следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле
# нужно выводить только первые n чисел, начиная с 1! и до n!.


def fact(arg):
    for i in range(1, arg + 1):
        result = 1
        for n in range(1, i + 1):
            result = result * n
        yield result


j = 1
for el in fact(6):
    print(f'{j}!  =  {el}')
    j += 1
