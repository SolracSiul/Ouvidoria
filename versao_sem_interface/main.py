#Esse é o arquivo solicitado para a criação do back-end da segunda atividade correspondente a ouvidoria!
import time

time = time.strftime('%H:%M')
timeSplit = time.split(':')
if int(timeSplit[0]) > 5  and int(timeSplit[0]) < 12:
    print('Bom dia')
elif int(timeSplit[0]) >= 12  and int(timeSplit[0]) < 18:
    print('Boa tarde')
elif int(timeSplit[0]) >= 18  and int(timeSplit[0]) < 5:
    print('Boa noite')

import versao_sem_interface.back as back

executando = True

while executando:
    print("#### OUVIDORIA ABC #### ")
    print("Opcoes: ")
    print("1) Listar todas as manifestações")
    print("2) Listar todas as sugestões")
    print("3) Listar todas as reclamações")
    print("4) Listar todos os elogios")
    print("5) Enviar uma manifestação (criar uma nova)")
    print("6) Pesquisar protocolo por número (ID)")
    print("7) Sair ")
    opcao = int(input("Informe uma opção: "))
    if type(opcao) is not int:
        print("digite um número")
    if opcao == 1:
        back.mostarManifestacoes()
    elif opcao == 2:
        back.mostrarSugestoes()
    elif opcao == 3:
        back.mostrarReclamacoes()
    elif opcao == 4:
        back.mostrarElogios()
    elif opcao == 5:
        back.criarManifestacoes()
    elif opcao == 6:
        back.buscarProtocolo()            
    elif opcao == 7:
        executando = False
    else:
        print("Opção invalida")
print("Programa encerrado")
print(back.manifestacoes)