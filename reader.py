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
from nltk.corpus import stopwords
from nltk import FreqDist


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

    def clean(self):
        pass
        # mail = self.find_emails()
        # links = self.find_all_links()
        # words = word_tokenize(self.all_text.lower())
        # cleanned = []
        # for word in words:
        #     if(word in mail or word in links):
        #         continue
        #     else:
        #         cleanned.append(word)

        # print(cleanned)

    def summarize(self):
        summary = ""
        stop_words = stopwords.words("english")
        words = word_tokenize(self.all_text.lower())
        sentences = sent_tokenize(self.all_text)
        sent_score = {}
        freq_table = {}
        # building frequency table
        for word in words:
            if(word.lower() not in stop_words):
                if(word.lower() not in string.punctuation):
                    if(word not in freq_table.keys()):
                        freq_table[word] = 1
                    else:
                        freq_table[word] += 1
        # devide by max
        max_freq = max(freq_table.values())
        for word in freq_table.keys():
            freq_table[word] = freq_table[word]/max_freq
        # ranking each sentence
        for sent in sentences:
            for word in sent:
                if (word.lower() in freq_table.keys()):
                    if (sent not in sent_score.keys()):
                        sent_score[sent] = freq_table[word.lower()]
                    else:
                        sent_score[sent] += freq_table[word.lower()]
        return sent_score
