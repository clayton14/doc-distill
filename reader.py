"""
Reads pdf file and extracts info and summorizes it
"""
import os
import sys
import string
import pandas
import numpy as np
from PyPDF2 import PdfFileReader
from nltk import sent_tokenize, word_tokenize
from transformers import pipeline


class Reader():
    def __init__(self, file=None,):
        self.file = file
        self.all_text = ""
        self.title = ""
        self.text_on_page = []
        self.read()

    def read(self):
        """
        Reads pdf file and extracts text
        """
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

    def extract_sentences(self):
        return sent_tokenize(self.all_text)

    def find_email(self):
        pass

    def find_all_links(self):
        pass

    def summarize(self):
        summory = ""
        summorizer = pipeline("summarization")
        for _, page in enumerate(self.text_on_page):
            summory += summorizer(page, max_length=130,
                                  min_length=30, do_sample=False)[0]['summary_text']
        return summory
