def leiaint():
    a = b = 0
    while True:
        try:
            a = int(input('Digite um inteiro: '))
        except Exception as ValueError:
                print('Erro! Por favor digite um número inteiro válido.')
        except KeyboardInterrupt:
            a = 0
            print()
            print('O usuário preferiu não digitar esse número.')
            break
        else:
            break
    while True:
        try:
            b = float(input('Digite um Real: '))
        except Exception as ValueError:
            print('Erro! Por favor digite um número real válido.')
            b = 0
        except KeyboardInterrupt:
            b = 0
            print()
            print('O usuário preferiu não digitar esse número.')
            break
        else:
            break
    print(f'O valor inteiro digitado foi {a} e o real foi {b}')


leiaint()
