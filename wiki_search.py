import wikipedia
import os
import sys
import random
from wikipedia import PageError
from wikipedia import DisambiguationError
import warnings
# TODO : make a more well rounded web scraping tool
# add GUI maye
# add google docs support


def search_wik(search_terms, num_sentance, output="out.txt"):
    print("======Starting======")
    assert len(search_terms) != 0, "List is empty"
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


# listh of this to to look up example x = ["minecraft", "Jacob Riis"]

x = [
    "sprawl", "load bearing masonry"
]

if __name__ == "__main__":
    search_wik(x, 3, output="out.txt")
# earch_test()
