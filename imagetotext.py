from cv2 import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
img=cv2.imread('Endsem.png')
text=pytesseract.image_to_string(img)
print(text)
