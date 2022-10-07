"""
python scrypt used to summorise websites givein a url
Work in progress
"""

import requests
from bs4 import BeautifulSoup
import os, sys, re
#from transformers import pipeline
import argparse
#transformers.utils.move_cache()
#=summarizer = pipeline("summarization", model="facebook/bart-large-cnn") 


def get_text(urls):
    """Pulls text from website"""
    responce = requests.get(urls)
    print("URL: ", responce.url , " Status Code:", responce.status_code)
    
    soup = BeautifulSoup(responce.text, "lxml")
    p_tags = soup.find_all('p')
    for tag in p_tags:
        site_text = tag.text.strip()

    return site_text


def get_description(url):
    pass


def summarize(text):
    return summarizer(text, min_length=50, do_sample=False)



if __name__ == "__main__":
    url = "https://laion.ai/blog/laion-5b/"
    #url = "https://shorturl.at/bjr25"
    x = get_text(url)  
    print(x) 
    #print(summarize(x))
    