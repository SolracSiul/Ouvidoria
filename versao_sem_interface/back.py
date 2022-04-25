#Esse arquivo é responsável por fornecer as funções para o arquivo main,py

manifestacoes = list()
usuario = dict()

def mostarManifestacoes():
        for x in manifestacoes:
            print(' Codigo ' + str(x['id']), end='/')
            print(' Requisitante: ' + x['requisitante'], end='/')
            print(' Tipo ' + x['tipo'], end='/')
            print(' Descrição '+ x['descricao'])
        else:
            print("Nenhuma manifestação encontrada!")
def mostrarSugestoes():
    for x in manifestacoes:
            if x['tipo'] == "Sugestão":
                print('codigo ' + str(x['id']), end='-')
                print(' Requisitante: ' + x['requisitante'], end='-')
                print(' Descrição ' + x['descricao'])
    else:
        print("Nenhuma sugestão encontrada!")
def mostrarReclamacoes():
    for x in manifestacoes:
            if x['tipo'] == "Reclamação":
                print('codigo ' + str(x['id']), end='-')
                print(' Requisitante: ' + x['requisitante'], end='-')
                print(' Descrição ' + x['descricao'])
    else:
        print("Nenhuma reclamação encontrada!")
def mostrarElogios():
    for x in manifestacoes:    
            if x['tipo'] == "Elogio":
                print('codigo ' + str(x['id']), end='-')
                print(' Requisitante: ' + x['requisitante'], end='-')
                print(' Descrição ' + x['descricao'])
    else:
        print("Nenhum elogio encontrado!")
def criarManifestacoes():
    executando5 = True
    while executando5:
        usuario.clear()
        usuario['id'] = len(manifestacoes)+1
        usuario['requisitante'] = str(input('Informe seu nome: '))
        print("Informe qual o tipo da sua manifestação")
        print("1)Reclamação")
        print("2)Sugestão")
        print("3)Elogio")
        executandoTipo = True
        while executandoTipo:
            #criar uma condicional para receber apenas numero!
            tipo = input("Digite o número: ")
            if tipo == '1':
                usuario['tipo'] = "Reclamação"
                executandoTipo = False
            elif tipo == '2':
                usuario['tipo'] = "Sugestão"
                executandoTipo = False
            elif tipo == '3':
                usuario['tipo'] = "Elogio"
                executandoTipo = False        
            else:
                print("Informe um numero no intervalo entre 1 e 3")
            usuario['descricao'] = str(input("Digite sua observação: "))
            manifestacoes.append(usuario.copy())
            executando5 = False
def buscarProtocolo():
    id = int(input("Informe o numero de protocolo desejado: "))
    for x in manifestacoes:
        if x['id'] == id:
            print(' Codigo ' + str(x['id']), end='/')
            print(' Requisitante: ' + x['requisitante'], end='/')
            print(' Tipo ' + x['tipo'], end='/')
            print(' Descrição '+ x['descricao'])

