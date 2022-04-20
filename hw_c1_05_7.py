# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).

import json

result = {}
average_profit = 0
numbers = 0
with open('text_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, form_of_own, revenue, costs = line.split()
        profit = float(revenue) - float(costs)
        if profit >= 0:
            average_profit += profit
            numbers += 1
        result[name] = profit
average_profit /= numbers
with open('result_ex_7.txt', 'w', encoding='utf-8') as file:
    json.dump([result, {'average_profit': average_profit}], file, ensure_ascii=False, indent = 4)
