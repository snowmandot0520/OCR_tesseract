import os
import sys
from pathlib import Path
import pandas as pd

# Add the project root directory to the Python path
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root / 'config'))

from preprocess import preprocess_image
from ocr import extract_text
from extract import extract_fields
from config import TESSERACT_CMD, INVOICE_DIR, OUTPUT_FILE

def process_invoice(image_path):
    image = preprocess_image(image_path)
    text = extract_text(image)
    extracted_data = extract_fields(text)
    return extracted_data

def save_to_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    invoice_dir = Path(INVOICE_DIR)
    invoice_paths = [invoice_dir / image_name for image_name in invoice_dir.iterdir() if image_name.is_file()]

    extracted_data_list = []

    for invoice_path in invoice_paths:
        extracted_data = process_invoice(invoice_path)
        extracted_data_list.append(extracted_data)

    save_to_excel(extracted_data_list, OUTPUT_FILE)
