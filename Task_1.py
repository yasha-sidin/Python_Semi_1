n = int(input('Введите количество километров, которое произжает машина за день: '))

m = int(input('Введите длину маршрута: '))

# result = int((m / n) + 0.9999)
# print(result)

# second solve 

result = (m - 1) // n + 1
print(result)