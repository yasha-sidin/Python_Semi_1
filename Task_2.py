# 2) 3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

print('Введите количество учеников: ')

n1 = int(input('First class: '))
n2 = int(input('Second class: '))
n3 = int(input('Third class: '))

# result = int((n1 + n2 + n3) / 2 + 0.9999)

tables1 = (n1 + 1) // 2
tables2 = (n2 + 1) // 2
tables3 = (n3 + 1) // 2
result = tables1 + tables2 + tables3

print(result)