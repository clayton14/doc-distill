"""
Reads pdf file and extracts info
"""
import os
import sys
import pandas
from PyPDF2 import PdfFileReader
"""
Reads PDF file and extracts info
"""


class Reader():
    def __init__(self, file=None,):
        self.file = file
        self.all_text = ""
        self.title = ""
        self.text_on_page = []
        self.images = []

    def read(self):
        try:
            with open(self.file, 'rb') as pdf_file:
                print(f"[READING] {self.file}")
                doc = PdfFileReader(pdf_file)
                for i in range(doc.numPages):
                    page = doc.getPage(i)
                    self.text_on_page.append(page.extractText())
                    self.all_text += page.extractText()
        except FileNotFoundError as err:
            print("[ERROR] file not found")

    def get_table(self, page_num):
        pass

    def summarize(self, text):
        pass
