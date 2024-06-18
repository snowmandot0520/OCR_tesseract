import os

# Path to Tesseract executable
TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Paths for input and output directories
INVOICE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'invoices')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'output', 'invoices.xlsx')
