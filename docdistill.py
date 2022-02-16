# Contains the main loop for the framwork
#
import os
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
from heapq import nlargest



"""
Reads pdf file and extracts info and summorizes it
"""
import os
import sys
import string
import pandas
import re
from PyPDF2 import PdfFileReader
import requests
import bs4
import lxml
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
from heapq import nlargest


"""
The reader class is resposable for reading PDF and web docs
"""
all_text = ""
title = ""
text_on_page = []
summary = ""


def read(src ):
    """
    Reads pdf file and extracts text or extrects text from websight
    """
    all_text = ""
    if(os.path.isfile(src)):
        try:
            with open(src, 'rb') as pdf_file:
                print(f"[READING] {src}")
                doc = PdfFileReader(pdf_file)
                for i in range(doc.numPages):
                    page = doc.getPage(i)
                    text_on_page.append(page.extractText())
                    all_text += page.extractText()
        except FileNotFoundError as err:
            print("[ERROR] file not found")
    return all_text


def _clean(self):
        emails = find_emails()
        links = find_emails()
        for link in links:
            all_text = all_text.replace(link, "")
        for mail in emails:
            all_text = all_text.replace(mail, "")

def _setup():
    pass
    #TODO check if nltk stuff is installed the download what is needed


def get_table(self, page_num):
    print("in dev")

def extract_sentences(self):
    return sent_tokenize(all_text)

def find_emails(self):
    mail_list = []
    regix = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    email_find = re.findall(regix, all_text)
    if (email_find):
        return email_find
    else:
        return []

def find_links(self):
    regix = "(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"
    links = re.findall(regix, all_text)
    if (links):
        return links
    else:
        return []


# TODO add more functions and maybe use google T5
def summarize(self, size=3):
    _clean()
    summary = ""
    stop_words = stopwords.words("english")
    words = word_tokenize(all_text.lower())
    sentences = sent_tokenize(all_text)
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

    for i in range(size):
        largest = nlargest(size, sent_score, key=sent_score.get)
        summary = ''.join(largest)
    return summary.replace("\n", "")
    # return freq_table



