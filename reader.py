"""
Reads pdf file and extracts info and summorizes it
"""
import os
import sys
import string
import pandas
import re
from PyPDF2 import PdfFileReader
from nltk import sent_tokenize, word_tokenize
from nltk.probability import ConditionalFreqDist
from nltk.corpus import stopwords


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
        print("in dev")

    def extract_sentences(self):
        return sent_tokenize(self.all_text)

    def find_emails(self):
        regix = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        mail_list = []
        email_find = re.findall(regix, self.all_text)
        for email in email_find:
            if(email in mail_list):
                continue
            else:
                mail_list.append(email)
        return mail_list

    def find_all_links(self):
        regix = "(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"
        links = re.findall(regix, self.all_text)
        if links:
            return links
        else:
            return "no URLs found"

    def clean():
        print("in dev")

    def summarize(self):
        stop_words = stopwords.words("english")
        print(stop_words)
