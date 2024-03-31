import webbrowser
try:
    webbrowser.open('https://pudim.com.br')
except:
    print('Não consegui acessar o site pudim.')
else:
    print('Consegui!')