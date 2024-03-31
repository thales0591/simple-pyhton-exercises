s = 0
f = 0
for c in range(1, 501):
    calc = c % 2
    mtres = c % 3
    if mtres == 0 and calc != 0:
        f += 1
        s = s + c
print(s, f)