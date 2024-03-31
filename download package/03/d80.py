num = []
for c in range(0, 5):
    a = int(input(f'Digite o valor {c+1}: '))
    if c == 0:
        num.append(a)
    elif c == 1:
        if a > num[0]:
            num.insert(1, a)
        elif a < num[0]:
            num.insert(0, a)
        else:
            num.insert(c - 1, a)
    elif c == 2:
        if num[0] < a < num[1]:
            num.insert(1, a)
        elif a < num[0]:
            num.insert(0, a)
        elif a > num[1]:
            num.insert(2, a)
        else:
            num.insert(c-1, a)
    elif c == 3:
        if num[0] < num[1] < a < num[2]:
            num.insert(2, a)
        elif num[0] < a < num[1] < num[2]:
            num.insert(1, a)
        elif a < num[0]:
            num.insert(0, a)
        elif a > num[2]:
            num.insert(3, a)
        else:
            num.insert(c-1, a)
    elif c == 4:
        if num[0] < num[1] < num[2] < a < num[3]:
            num.insert(3, a)
        elif num[0] < num[1] < a < num[2] < num[3]:
            num.insert(2, a)
        elif num[0] < a < num[1] < num[2] < num[3]:
            num.insert(1, a)
        elif a < num[0]:
            num.insert(0, a)
        elif a > num[3]:
            num.insert(4, a)
        else:
            num.insert(c-1, a)
print(num)
