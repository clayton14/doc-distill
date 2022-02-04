"""
Reads pdf file and extracts info
"""
import os
import sys
from PyPDF2 import PdfFileReader


class Reader():
    def __init__(self, file=None,):
        self.file = file
        self.all_text = None
        self.page_text = []
        self.images = []

    def read(self):
        try:
            with open(self.file, 'rb') as pdf_file:
                doc = PdfFileReader(pdf_file)

                # if("not scaned"):
                #     # PyPdf
                #     pass
                # else:
                #     # use ocr
                #     pass
        except FileNotFoundError as err:
            print("[ERROR] file not found")

    def extract_images():
        pass
