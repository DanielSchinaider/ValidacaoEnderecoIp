# Desenvolvido por Daniel Schinaider de Oliveira

from collections import OrderedDict
# Instacia
vetorA = []
vetorB = []
vetorC = []

# Funcao responsável por ler o arquivo de texto no caminho especificado
def readFile():
    nome_arquivo = "C:\\Users\\Aluno\\enderecoIp.txt"

    f = open(nome_arquivo, 'r')
    texto = f.readlines()
    return texto

# Funcao responsavel por criar arquivo de texto com enderecos ip validos e invalido dentro do caminho especificado
def createFile(texto):
    nome_arquivo = "C:\\Users\\Aluno\\relatorioIps.txt"
    f = open(nome_arquivo, 'w+')
    for i in range(len(texto)):
        f.write(texto[i])
    f.close()
    return 0

# Funcao responsavel por verificar se endereco Ip é de classe A
def ipClassA(texto):
    aux = ""
    ips = ""
    vetorA = []
    for i in range(len(texto)):
        # Variavel recebe ip da posicao do vetor
        ips = texto[i]
        aux = texto[i]
        # Varivel desmonta o ip em pontos, gerando posicoes
        ips = ips.split(".")
        # Condicao para verificar se os valores dos octetos
        if int(ips[0]) == 10:
            if int(ips[1]) >= 0 and int(ips[1]) <= 255:
                if int(ips[2]) >= 0 and int(ips[2]) <= 255:
                    if int(ips[3]) >= 0 and int(ips[3]) <= 255:
                        # Caso o endereco seja de classe A ela vai para o vetor A
                        vetorA.append(aux)

    return vetorA

# Funcao responsavel por verificar se endereco Ip é de classe B
def ipClassB(texto):
    aux = ""
    ips = ""
    vetorB = []
    for i in range(len(texto)):
        # Variavel recebe ip da posicao do vetor
        ips = texto[i]
        aux = texto[i]
        # Varivel desmonta o ip em pontos, gerando posicoes
        ips = ips.split(".")
        # Condicao para verificar se os valores dos octetos
        if int(ips[0]) == 172:
            print(ips)
            if int(ips[1]) >= 16 and int(ips[1]) <= 31:
                if int(ips[2]) >= 0 and int(ips[2]) <= 255:
                    if int(ips[3]) >= 0 and int(ips[3]) <= 255:
                        # Caso o endereco seja de classe A ela vai para o vetor B
                        vetorB.append(aux)
    return vetorB

# Funcao responsavel por verificar se endereco Ip é de classe B
def ipClassC(texto):
    aux = ""
    ips = ""
    vetorC = []
    for i in range(len(texto)):
        # Variavel recebe ip da posicao do vetor
        ips = texto[i]
        aux = texto[i]
        # Varivel desmonta o ip em pontos, gerando posicoes
        ips = ips.split(".")
        # Condicao para verificar se os valores dos octetos
        if int(ips[0]) == 192:
            if int(ips[1]) == 168:
                if int(ips[2]) >= 0 and int(ips[2]) <= 255:
                    if int(ips[3]) >= 0 and int(ips[3]) <= 255:
                        # Caso o endereco seja de classe A ela vai para o vetor C
                        vetorC.append(aux)

    return vetorC

# Funcao responsavel por deletar itens repetidos da lista
def remove_repetidos(l):
    # Variavel recebe os valores da lista
    lista = l
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[j] == lista[i]:
                # Caso o valor seja encontrado novamente na lista ele é deletado
                del(lista[j])
            else:
                j = j + 1
        i = i + 1
# Retorna a lista em forma crescente
    return sorted(lista)

# Funcao responsavel pela validacao de enderecos valido e invalidos
def validation(texto):
    # Vetor recebem o retorno das funcoes que validam pela classe
    vetorA = ipClassA(texto)
    vetorB = ipClassB(texto)
    vetorC = ipClassC(texto)

    vetorValid = []
    vetorinvalid = []
    text = []
    # Loor para verificar se valores dos vetores se encontram no vetor que recebe todos endereco Ip
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
    # Vetor recebe todos enderecos Ip
    for i in range(len(texto)):
        vetorinvalid.append(texto[i])
    # Loop para pegar posicao de valores que sao validos
    for a in range(len(vetorValid)):
        for e in range(len(vetorinvalid)):
            # Condicao para verificar se item da lista de enderecos validos se encontra em lista dos invalidos
            if vetorValid[a] == vetorinvalid[e]:
                #Condicao que verifica o tamanho do vetor auxiliar
                if len(vetorAux) == 0:
                    # caso o tamanho seja 0 ele adiciona a primeira posicao na lista
                    vetorAux.append(e)
                elif len(vetorAux) > 0:
                    # caso seja maior ele adiciona a que ele encontrar
                        vetorAux.append(e)
                continue
            else:
                continue
    # Condicao para verificar se vetor auxiliar é maior que 0
    if len(vetorAux) > 0:
        # vetor auxiliar adiciona item que retornam da funcao remove repetidos
        vetorAux = remove_repetidos(vetorAux)
    # Loop para remover itens validos da lista de invalidos
    for i in range(len(vetorAux)):
        j = i
        if i == 0:
            # caso i seja 0 ele remove normalmente
            vetorinvalid.remove((vetorinvalid[vetorAux[j]]))
        elif i > 0:
            # caso i for maior ele faz remocao de forma diferente
            index = 0
            # condicao verificando se valor do vetor auxiliar for maior que 1
            if vetorAux[i] > 1:
                # caso seja, o index recebe o valor do vetor auxiliar subtraido por i
                index = (vetorAux[i] - i)
            else:
                # caso não seja, o index recebe apenas o valor do vetor auxiliar
                index = vetorAux[i]
            # Vetor dos enderecos invalidos remove todos itens que tiverem na posicao especificada pelo index
            vetorinvalid.remove((vetorinvalid[index]))

# Vetor final adiciona um primeiro texto
    text.append("[Enderecos Válidos:]\n")
    # vetor final adiciona todos valores de vetor dos enderecos válidos
    for w in range(len(vetorValid)):
        text.append(vetorValid[w])
    # Vetor final adiciona um segundo texto
    text.append("\n[Enderecos Inválidos:]\n")
    # vetor final adiciona todos valores de vetor dos enderecos inválidos
    for q in range(len(vetorinvalid)):
        text.append(vetorinvalid[q])
# retorna a lista final toda validada
    return text

# variaveis que armazenam valores retornados da funcoes
texto = readFile()
escrever = validation(texto)
# chamada da funcao para criar arquivo texto
createFile(escrever)
