import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PIL import Image

app = QApplication(sys.argv)
janela = QWidget()
janela.resize(500, 600)

imgFilme = QLabel('Vacalo patas duas', janela)
imgFilme.setPixmap(QPixmap('gif-louco-cavalo.webp'))


#redimencionando a imagem
imgFilmeNovo = Image.open('gif-louco-cavalo.webp')
largura = imgFilmeNovo.width * 3
altura = imgFilmeNovo.height * 3
imagemRedimencionada = imgFilmeNovo.resize((largura, altura))
imagemRedimencionada.save('Nova imagemvacalo2.jpg')

#exibir nova imagem
imgFilme2 = QLabel('Vacalo2',janela)
imgFilme2.setPixmap(QPixmap('Nova imagemvacalo2.jpg'))


janela.show()
app.exec()