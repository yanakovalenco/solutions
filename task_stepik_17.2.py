# Вам доступен текстовый файл prices.txt с информацией о заказе из интернет-магазина.
# В нем каждая строка с помощью символа табуляции (\t) разделена на три колонки:
# - наименование товара;
# - количество товара (целое число);
# - цена (в рублях) товара за 11 шт. (целое число).
# Напишите программу, выводящую на экран общую стоимость заказа.
#
# Формат входных данных: На вход программе ничего не подается.
# Формат выходных данных: Программа должна вывести общую стоимость заказа.
# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

file = open('prices.txt', 'r', encoding='utf-8')
content = []
for line in file:
    content.append(line.split('\t'))
res = list(map(lambda x: int(x[1]) * int(x[2]), content))
print(sum(res))
file.close()
