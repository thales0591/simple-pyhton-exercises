def notas(*num, sit=False):
    dicio = dict()
    dicio['total'] = len(num)
    maior = menor = soma = 0
    for d in num:
        soma += d
        if d == num[0]:
            maior = d
            menor = d
        else:
            if d > maior:
                maior = d
            if d < menor:
                menor = d
    dicio['maior'] = maior
    dicio['menor'] = menor
    dicio['média'] = f'{soma / len(num):.3f}'
    if sit:
        if float(dicio['média']) >= 7:
            dicio['situação'] = 'BOA'
        elif 5 < float(dicio['média']) < 7:
            dicio['situação'] = 'Razoável'
        else:
            dicio['situação'] = 'Ruim'
    return dicio


resp = notas(3.5, 6.5, 2, 7, 4, 2)
print(resp)
