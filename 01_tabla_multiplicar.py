number = input('Give me a number: \n')
number = int(number)

for n in range(10):
    r = number * (n + 1)
    print(f'{number} * {n + 1} = {r}')
    