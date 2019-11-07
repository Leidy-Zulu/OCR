try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))  # pytesseract es usado para detectar cadena de caracteres en la imagen
    return text 
