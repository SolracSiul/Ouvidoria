from PyQt5 import uic, QtWidgets
from user import Usuario
import mysql.connector

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulariov2.ui")
tela_listar_items=uic.loadUi("funcoes.ui")

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="luis",
    database="appClasse"
)

comandos_banco = banco.cursor()
def criar():
    Usuario.nome = formulario.lineEdit_2.text()
    Usuario.descricao = formulario.lineEdit_4.text()
    if formulario.radioButton.isChecked():
        Usuario.tipo = "reclamação"
    elif formulario.radioButton_2.isChecked():
        Usuario.tipo = "sugestão"
    elif formulario.radioButton_3.isChecked():
        Usuario.tipo = "elogio"
    
    print()
    comando_SQL = "INSERT INTO usuarios (nome,descricao, tipo) VALUES(%s,%s,%s)"
    dados = (str(Usuario.nome),str(Usuario.descricao),Usuario.tipo)
    comandos_banco.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_4.setText("")
    print("Foi adicionado um novo elemento ao banco de dados")
    print("O elemento é: ")
    print("O nome é: ",Usuario.nome,"-","O tipo da manifestação é: ","-",Usuario.tipo,"A descrição é:","-",Usuario.descricao)

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


formulario.pushButton.clicked.connect(criar)
formulario.pushButton_2.clicked.connect(listar_manifestacoes)
formulario.pushButton_3.clicked.connect(listar_sugestao)
formulario.pushButton_4.clicked.connect(listar_reclamacoes)
formulario.pushButton_5.clicked.connect(listar_elogios)
formulario.pushButton_6.clicked.connect(buscar_por_id)

formulario.show()
app.exec()
#print(Usuario.nome, Usuario.descricao, Usuario.tipo)
