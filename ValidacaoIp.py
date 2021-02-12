from collections import OrderedDict

vetorA = []
vetorB = []
vetorC = []


def readFile():
    nome_arquivo = "C:\\Users\\Aluno\\enderecoIp.txt"

    f = open(nome_arquivo, 'r')
    texto = f.readlines()
    return texto


def createFile(texto):
    nome_arquivo = "C:\\Users\\Aluno\\relatorioIps.txt"
    f = open(nome_arquivo, 'w+')
    for i in range(len(texto)):
        f.write(texto[i])
    f.close()
    return 0


def ipClassA(texto):
    aux = ""
    ips = ""
    vetorA = []
    for i in range(len(texto)):
        ips = texto[i]
        aux = texto[i]
        ips = ips.split(".")
        if int(ips[0]) == 10:
            if int(ips[1]) >= 0 and int(ips[1]) <= 255:
                if int(ips[2]) >= 0 and int(ips[2]) <= 255:
                    if int(ips[3]) >= 0 and int(ips[3]) <= 255:
                        vetorA.append(aux)

    return vetorA


def ipClassB(texto):
    aux = ""
    ips = ""
    vetorB = []
    for i in range(len(texto)):
        ips = texto[i]
        aux = texto[i]
        ips = ips.split(".")
        if int(ips[0]) == 172:
            print(ips)
            if int(ips[1]) >= 16 and int(ips[1]) <= 31:
                if int(ips[2]) >= 0 and int(ips[2]) <= 255:
                    if int(ips[3]) >= 0 and int(ips[3]) <= 255:
                        vetorB.append(aux)
                        print(vetorB)

    return vetorB


def ipClassC(texto):
    aux = ""
    ips = ""
    vetorC = []
    for i in range(len(texto)):
        ips = texto[i]
        aux = texto[i]
        ips = ips.split(".")
        if int(ips[0]) == 192:
            if int(ips[1]) == 168:
                if int(ips[2]) >= 0 and int(ips[2]) <= 255:
                    if int(ips[3]) >= 0 and int(ips[3]) <= 255:
                        vetorC.append(aux)

    return vetorC


def remove_repetidos(l):

    lista = l
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[j] == lista[i]:
                del(lista[j])
            else:
                j = j + 1
        i = i + 1

    return sorted(lista)

def validation(texto):
    vetorA = ipClassA(texto)
    vetorB = ipClassB(texto)
    vetorC = ipClassC(texto)

    vetorValid = []
    vetorinvalid = []
    text = []
    for i in range(0, len(texto)):
        for a in range(len(vetorA)):
            if vetorA[a] == texto[i]:
                vetorValid.append(texto[i])
                break
            else:
                continue
        for e in range(len(vetorB)):
            if vetorB[e] == texto[i]:
                vetorValid.append(texto[i])
                break
            else:
                continue
        for o in range(len(vetorC)):
            if vetorC[o] == texto[i]:
                vetorValid.append(texto[i])
                break
    aux = 0
    vetorAux = []

    for i in range(len(texto)):
        vetorinvalid.append(texto[i])

    for a in range(len(vetorValid)):
        for e in range(len(vetorinvalid)):
            if vetorValid[a] == vetorinvalid[e]:
                if len(vetorAux) == 0:
                    vetorAux.append(e)
                elif len(vetorAux) > 0:
                        vetorAux.append(e)
                continue
            else:
                continue

    if len(vetorAux) > 0:
        vetorAux = remove_repetidos(vetorAux)

    for i in range(len(vetorAux)):
        j = i
        if i == 0:
            vetorinvalid.remove((vetorinvalid[vetorAux[j]]))
        elif i > 0:
            index = 0
            if vetorAux[i] > 1:
                index = (vetorAux[i] - i)
            else:
                index = vetorAux[i]
            vetorinvalid.remove((vetorinvalid[index]))

    text.append("[Enderecos Válidos:]\n")
    for w in range(len(vetorValid)):
        text.append(vetorValid[w])
    text.append("\n[Enderecos Inválidos:]\n")
    for q in range(len(vetorinvalid)):
        text.append(vetorinvalid[q])

    return text

texto = readFile()
escrever = validation(texto)
createFile(escrever)
