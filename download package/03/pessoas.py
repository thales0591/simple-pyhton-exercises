lista = list
cop = list()
cop2 = []


def registro(nom='', ida=0):
    global lista
    global cop
    cop.append(nom)
    cop.append(ida)


print(cop)