num = []
for c in range(0, 5):
    a = int(input('Digite um número: '))
    if c == 0 or a > num[-1]:
        num.append(a)
    else:
        cont = 0
        while cont < len(num):
            if a <= num[cont]:
                num.insert(cont, a)
                break
            cont += 1
print(num)
