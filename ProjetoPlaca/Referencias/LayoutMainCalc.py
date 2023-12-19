#importacoes
import sys
from PyQt6.QtWidgets import *
#-------------------------------------------------------------------------------------


#janela
app = QApplication(sys.argv)
janela = QWidget()
#-------------------------------------------------------------------------------------


#variaveis auxiliares
Aux1 = QLineEdit('')
Aux2 = QLineEdit('')
AuxSinal = QLineEdit('')
#-------------------------------------------------------------------------------------


#Funcoes botoes

#ExibirDisplay
def ExibirNoDisplay(x):
    valor = DisplayExibir.text() + x
    DisplayExibir.setText(valor)

#Somar
def somar ():
    valor = DisplayExibir.text()
    Aux1.setText(valor)
    AuxSinal.setText('+')
    DisplayExibir.setText('')

#Subtracao
def subtrair ():
    valor = DisplayExibir.text()
    Aux1.setText(valor)
    AuxSinal.setText('-')
    DisplayExibir.setText('')

#Multiplicacao
def multiplicar ():
    valor = DisplayExibir.text()
    Aux1.setText(valor)
    AuxSinal.setText('*')
    DisplayExibir.setText('')

#Divisao
def dividir ():
    valor = DisplayExibir.text()
    Aux1.setText(valor)
    AuxSinal.setText('/')
    DisplayExibir.setText('')



#Funcoes calculos

#calcular
def calcular ():
    Aux2.setText(DisplayExibir.text())

    if AuxSinal.text() == '+':
        soma = float(Aux1.text()) + float(Aux2.text())
        DisplayExibir.setText('')
        DisplayExibir.setText(str(soma))
    
    elif AuxSinal.text() == '-':
        subtrair = float(Aux1.text()) - float(Aux2.text())
        DisplayExibir.setText('')
        DisplayExibir.setText(str(subtrair))

    elif AuxSinal.text() == '*':
        multiplicar = float(Aux1.text()) * float(Aux2.text())
        DisplayExibir.setText('')
        DisplayExibir.setText(str(multiplicar))

    elif AuxSinal.text() == '/':
        dividir = float(Aux1.text()) / float(Aux2.text())
        DisplayExibir.setText('')
        DisplayExibir.setText(str(dividir))
#-------------------------------------------------------------------------------------


#limpar
def limpar():
    DisplayExibir.setText('')
    Aux1.setText('')
    Aux2.setText('')
    AuxSinal.setText('')
#-------------------------------------------------------------------------------------

#chamada style.css
with open('style.css', 'r') as file:
    app.setStyleSheet(file.read())
#-------------------------------------------------------------------------------------

#display
DisplayExibir = QLineEdit('', janela)
DisplayExibir.setGeometry(10, 10, 280, 50)
#-------------------------------------------------------------------------------------

#BotoesNumero primeira linha (7,8,9)
Botao7 = QPushButton ('7', janela)
Botao7.setGeometry(10, 70, 60, 60)
Botao7.clicked.connect(lambda:ExibirNoDisplay('7'))

Botao8 = QPushButton ('8', janela)
Botao8.setGeometry(80, 70, 60, 60)
Botao8.clicked.connect(lambda:ExibirNoDisplay('8'))

Botao9 = QPushButton ('9', janela)
Botao9.setGeometry(150, 70, 60, 60)
Botao9.clicked.connect(lambda:ExibirNoDisplay('9'))
#-------------------------------------------------------------------------------------


#BotoesNumero segunda linha (4,5,6)
Botao4 = QPushButton ('4', janela)
Botao4.setGeometry(10, 140, 60, 60)
Botao4.clicked.connect(lambda:ExibirNoDisplay('4'))

Botao5 = QPushButton ('5', janela)
Botao5.setGeometry(80, 140, 60, 60)
Botao5.clicked.connect(lambda:ExibirNoDisplay('5'))

Botao6 = QPushButton ('6', janela)
Botao6.setGeometry(150, 140, 60, 60)
Botao6.clicked.connect(lambda:ExibirNoDisplay('6'))
#-------------------------------------------------------------------------------------

#BotoesNumero terceira linha (1,2,3)
Botao1 = QPushButton ('1', janela)
Botao1.setGeometry(10, 210, 60, 60)
Botao1.clicked.connect(lambda:ExibirNoDisplay('1'))

Botao2 = QPushButton ('2', janela)
Botao2.setGeometry(80, 210, 60, 60)
Botao2.clicked.connect(lambda:ExibirNoDisplay('2'))

Botao3 = QPushButton ('3', janela)
Botao3.setGeometry(150, 210, 60, 60)
Botao3.clicked.connect(lambda:ExibirNoDisplay('3'))
#-------------------------------------------------------------------------------------


#BotoesNumero quarta linha (0, c, .)
BotaoC = QPushButton ('C', janela)
BotaoC.setGeometry(10, 280, 60, 60)
BotaoC.clicked.connect(limpar)

Botao0 = QPushButton ('0', janela)
Botao0.setGeometry(80, 280, 60, 60)
Botao0.clicked.connect(lambda:ExibirNoDisplay('0'))

BotaoPonto = QPushButton ('.', janela)
BotaoPonto.setGeometry(150, 280, 60, 60)
BotaoPonto.clicked.connect(lambda:ExibirNoDisplay('.'))
#-------------------------------------------------------------------------------------


#BotaoIgual
BotaoIgual = QPushButton ('=', janela)
BotaoIgual.setGeometry(10, 350, 280, 60)
BotaoIgual.clicked.connect(calcular)
#-------------------------------------------------------------------------------------


#BotoesOperacoes

#Subtracao
BotaoMenos = QPushButton('-', janela)
BotaoMenos.setGeometry(230, 70, 60, 60)
BotaoMenos.clicked.connect(subtrair)

#Soma
BotaoMais = QPushButton('+', janela)
BotaoMais.setGeometry(230, 140, 60, 60)
BotaoMais.clicked.connect(somar)

#Divisao
BotaoDiv = QPushButton('÷', janela)
BotaoDiv.setGeometry(230, 210, 60, 60)
BotaoDiv.clicked.connect(dividir)

#Multiplicacao
BotaoMulti = QPushButton('x', janela)
BotaoMulti.setGeometry(230, 280, 60, 60)
BotaoMulti.clicked.connect(multiplicar)
#-------------------------------------------------------------------------------------


#Abrir janela
janela.resize(300, 420)
janela.setWindowTitle('Calculadora')
janela.show()
app.exec()
#-------------------------------------------------------------------------------------
