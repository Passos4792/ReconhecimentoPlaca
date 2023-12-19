from PIL import Image
import cv2
import pytesseract
import pytesseract as orc

#C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR

def Reconhecer(imagem):
    #indicando o caminho da instalacao do pytesseract
    pytesseract.pytesseract.tesseract_cmd=r"C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    #pegar a imagem de uma placa
    placa  = cv2.imread (imagem,0)

    #converter texto de imagens em caracteres
    texto = pytesseract.image_to_string(placa, config='-l eng --oem 3 --psm 12')

    return texto
