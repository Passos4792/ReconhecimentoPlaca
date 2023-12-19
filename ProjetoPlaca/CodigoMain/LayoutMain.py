#importacoes
import Dados
import ReconhecerPlaca
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PIL import Image
import cv2
#-------------------------------------------------------------------------------------


#variaveis globais
DadosPessoas = Dados.informacoes()
#-------------------------------------------------------------------------------------


#janela
app = QApplication(sys.argv)
janela = QWidget()
#-------------------------------------------------------------------------------------


#funcoes
def buscar():
    #capturando imagens da camera padrao
    camera = cv2.VideoCapture(0)

    #capturando imagens de video
    # camera = cv2.VideoCapture('PlacasImagens/Video.mov')

    while True:
        sucesso, frame = camera.read()
        cv2.imshow('FrameCamera', frame)
        cv2.imwrite('teste.png', frame)

    #teste de verificacao de placa
        PlacaReconhecida = ReconhecerPlaca.Reconhecer('teste.png')
        for pe in DadosPessoas.keys():
            if pe in PlacaReconhecida:
                print (DadosPessoas[pe][0])
                DisplayExibirNome.setText(DadosPessoas[pe][0])
                DisplayExibirModelo.setText(DadosPessoas[pe][1])
                DisplayExibirAno.setText(str(DadosPessoas[pe][2]))
                DisplayExibirPlaca.setText(pe)
        if cv2.waitKey(1) & 0xFF == ord ('s'):
            break

#-------------------------------------------------------------------------------------


#chamada style.css
with open('CodigoMain/style.css', 'r') as file:
    app.setStyleSheet(file.read())
#-------------------------------------------------------------------------------------


#LabelReconhecimentoDePlaca
LabelReconhecimentoPlaca = QLabel('Reconhecimento de placa', janela)
LabelReconhecimentoPlaca.setGeometry(75, 20, 350, 35)
LabelReconhecimentoPlaca.setStyleSheet('Font-Size: 30px')

#-------------------------------------------------------------------------------------


#ImagemPlaca

imgPlaca = QLabel('Imagem Placa', janela)
imgPlaca.setPixmap(QPixmap('PlacasImagens/PlacaImagem1.png'))
imgPlaca.setGeometry(55, -100, 500, 500)
#-------------------------------------------------------------------------------------


#Labels

#LabelNome
LabelNome = QLabel('Nome:', janela)
LabelNome.setGeometry(60, 240, 50, 50)

#LabelModelo
LabelModelo = QLabel('Modelo:', janela)
LabelModelo.setGeometry(60, 290, 50, 50)

#LabelAno
LabelAno = QLabel('Ano:', janela)
LabelAno.setGeometry(60, 340, 50, 50)

#LabelPlaca
LabelPlaca = QLabel('Placa:', janela)
LabelPlaca.setGeometry(60, 390, 50, 50)
#-------------------------------------------------------------------------------------


#Caixas de texto

#DigitarNome
DisplayExibirNome = QLineEdit('', janela)
DisplayExibirNome.setGeometry(120, 250, 330, 35)

#DigitarModelo
DisplayExibirModelo = QLineEdit('', janela)
DisplayExibirModelo.setGeometry(120, 300, 330, 35)

#DigitarAno
DisplayExibirAno = QLineEdit('', janela)
DisplayExibirAno.setGeometry(120, 350, 330, 35)

#DigitarPlaca
DisplayExibirPlaca = QLineEdit('', janela)
DisplayExibirPlaca.setGeometry(120, 400, 330, 35)
#-------------------------------------------------------------------------------------


#BotaoVerificar
BotaoVerificar = QPushButton ('Verificar', janela)
BotaoVerificar.setGeometry
BotaoVerificar.setGeometry(50, 500, 400, 65)
BotaoVerificar.clicked.connect(buscar)

#Abrir janela
janela.resize(500, 600)
janela.setWindowTitle('Reconhecimento placa')
janela.show()
app.exec()
#-------------------------------------------------------------------------------------