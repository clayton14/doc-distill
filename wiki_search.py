#!/usr/bin/env python
__author__   = "Clayton Easley"
"""
cli tool to search terms on wikipedia and summarize them
"""

import wikipedia
import os
import sys
import random
from wikipedia import PageError
from wikipedia import DisambiguationError
import warnings
import argparse
# TODO : make a more well rounded web scraping tool
# add google docs support (maybe)


def search_wik(search_terms: list, num_sentance, output="out.txt"):
    print("======Starting======")
    assert len(search_terms) != 0, "List is empty"
    if not isinstance(search_terms, list): 
        print("[ERROR] the input is not of type list")
        sys.exit(1)
    else:
        pass
    # warnings.catch_warnings()
    # warnings.simplefilter("ignore")
    with open(os.path.join(os.getcwd(), output), "w+") as f:
        for term in search_terms:
            try:
                summary = wikipedia.summary(term, sentences=num_sentance)
                print(f"[DONE]: {term}")
                f.writelines(f"{term}:\n{summary}\n\n")
            except DisambiguationError as e:
                print(
                    f"[ERROR:{term}] multple things are related to {term}.\nDid you mean")
                for num, option in enumerate(e.options):
                    print(f"[{num}] {option}")
                index = int(
                    input("enter the number corresponding to the search term:\n"))
                summary = wikipedia.summary(
                    e.options[index], sentences=num_sentance)
                f.writelines(f"{option}:\n{summary}\n")
                print(f"[DONE]: {option}")
            except PageError as e:
                print(
                    f"[ERROR:{term}] page not found for {term}! try and make your search terms more specific\n")
                continue


def read_file(file) -> list:
    terms = []
    with open(file, 'r+',encoding='utf-8-sig') as f:
        #print(f.read())
        for line in f.readlines():
            if "\n" in line:
                line = line.replace('\n', '') 
            terms.append(line)
    return terms
        

# x = [
#     "sprawl", "load bearing masonry"
# ]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str,help="input a text file with list of terms to search")
    parser.add_argument("-n", type=int, help="the length of summary in number of sentances (default is 3)")
    parser.add_argument("-t", type=str, help="the term you want to serch")
    args = parser.parse_args()
    
    summ_len = 3

    if args.n and args.n < 20:
        summ_len = args.n
    # else:
    #     summ_len = 3
    #     print("summary too long -n must be less than 20")
    #     sys.exit(1) 

    if args.f:
        try:
            terms = read_file(args.f)
            search_wik(terms, summ_len)
        except FileNotFoundError() as e:
            print("[ERROR] file not found")

    if args.t:
        search_wik([args.t], summ_len)

    #terms = read_file("History Cold War.txt")
    #search_wik(["John Donne (poet)"] ,3)




