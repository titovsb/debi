isk = float(input('Сумма иска: '))
if isk <= 100000:
    res = isk * 0.04
    if res < 2000:
        res = 2000
elif 100001 <= isk <= 200000:
    res = (isk - 100000) * 0.03 + 4000   
elif 200001 <= isk <= 1000000:
    res = (isk - 200000) * 0.02 + 7000
elif 1000001 <= isk <= 2000000:
    res = (isk - 1000000) * 0.01 + 23000
elif isk >= 2000001:
    res = (isk - 2000000) * 0.005 + 33000
    if res > 200000:
        res = 200000
x = int(res + (0.5 if res > 0 else -0.5))
print(f'Госпошлина: {x}')