# Invoice Extractor

## Overview

This project extracts data from invoices and loads it into an Excel file. It uses Tesseract OCR to read text from invoice images and pandas to handle the data and export it to Excel.

## File Structure

- `config/`: Contains configuration files.
- `data/`: Contains raw invoice images and the output Excel file.
- `src/`: Contains the main scripts for preprocessing, OCR, and field extraction.
- `requirements.txt`: Lists the Python dependencies.
- `README.md`: Project documentation.

## Setup

1. Install Tesseract OCR:

   - On Windows: Download and install from [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki).
   - On macOS: Install using Homebrew `brew install tesseract`.
   - On Linux: Install via package manager, e.g., `sudo apt-get install tesseract-ocr`.

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```
