import pytesseract
from config import TESSERACT_CMD

pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text
