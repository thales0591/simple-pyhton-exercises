tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
         'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in tupla:
    vogais = ('a', 'e', 'i', 'o', 'u')
    print(f'\nNa palavra {p.upper()} temos:', end=' ')
    for c in range(0, len(p)):
        if p[c] in vogais:
            print(p[c], end=' ')