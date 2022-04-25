#Esse arquivo é responsável por realizar a conexão com o banco de dados e com a interface do usuário!

from PyQt5 import uic, QtWidgets
import mysql.connector

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulariov2.ui")
tela_listar_items=uic.loadUi("funcoes.ui")


banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="luis",
    database="bancoOuvidoria"
)

comandos_banco = banco.cursor()

usuarios = list()

def funcao_principal():
    print("Teste")
    nome = formulario.lineEdit_2.text()
    print("esse eh o nome cadastrado", nome)
    descricao = formulario.lineEdit_4.text()
    print("Essa eh a descrição do problema", descricao)
    tipo = ""
    if formulario.radioButton.isChecked():
        print("Tipo reclamação foi selecionado!")
        tipo = "reclamação"
    elif formulario.radioButton_2.isChecked():
        print("Tipo sugestão foi selecionado!")
        tipo = "sugestão"
    elif formulario.radioButton_3.isChecked():
        print("Tipo elogio foi selecionado!")
        tipo = "elogio"
    else:
        print("Selecione uma tipo")

    print("Descrição", descricao)

    comando_SQL = "INSERT INTO usuarios (nome, descricao, tipo) VALUES(%s,%s,%s)"
    dados = (str(nome),str(descricao),tipo)
    comandos_banco.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_4.setText("")

#listar todas as manifestações
def listar_manifestacoes():
    tela_listar_items.show()

    comando_SQL = "SELECT * FROM usuarios"
    comandos_banco.execute(comando_SQL)
    dados_lidos = comandos_banco.fetchall()
    print(dados_lidos)

    tela_listar_items.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_items.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            tela_listar_items.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
#listar sugestões


def listar_sugestao():
    tela_listar_items.show()
    
    comando_SQL = "SELECT * FROM usuarios WHERE tipo = 'sugestão'"
    comandos_banco.execute(comando_SQL)
    dados_lidos = comandos_banco.fetchall()
    print(dados_lidos)

    tela_listar_items.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_items.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            tela_listar_items.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def listar_reclamacoes(): 
    tela_listar_items.show()

    comando_SQL = "SELECT * FROM usuarios WHERE tipo = 'reclamação'"
    comandos_banco.execute(comando_SQL)
    dados_lidos = comandos_banco.fetchall()
    print(dados_lidos)

    tela_listar_items.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_items.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            tela_listar_items.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def listar_elogios():
    tela_listar_items.show()

    comando_SQL = "SELECT * FROM usuarios WHERE tipo = 'elogio'"
    comandos_banco.execute(comando_SQL)
    dados_lidos = comandos_banco.fetchall()
    print(dados_lidos)

    tela_listar_items.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_items.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            tela_listar_items.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def buscar_por_id():
    tela_listar_items.show()

    numero_id = formulario.lineEdit_3.text()
    comando_SQL = "SELECT * FROM usuarios WHERE Codigo = " + str(numero_id)
    comandos_banco.execute(comando_SQL)
    dados_lidos = comandos_banco.fetchall()
    print(dados_lidos)

    tela_listar_items.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_items.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            tela_listar_items.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))



formulario.pushButton_2.clicked.connect(listar_manifestacoes)
formulario.pushButton_3.clicked.connect(listar_sugestao)
formulario.pushButton_4.clicked.connect(listar_reclamacoes)
formulario.pushButton_5.clicked.connect(listar_elogios)
formulario.pushButton_6.clicked.connect(buscar_por_id)
formulario.pushButton.clicked.connect(funcao_principal)


formulario.show()
app.exec()