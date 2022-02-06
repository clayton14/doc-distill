# Contains the main loop for the framwork
#
import pyfiglet
import random


def main():
    while True:
        start = input(">>>")
        if(start == "help"):
            print(
                "options:\nweb\tinput the url to a website to extract text\nfind\tsearch for PDF in current dir")
        elif(start == "web"):
            web_input = input("[URL]>>>")
        elif(start == "find"):
            print("looking for PDF docuiment in current dir")


if __name__ == "__main__":
    art = ["smisome1", "5lineoblique", "block", "larry3d"]
    print(pyfiglet.figlet_format("DocDistill", font=random.choice(art)))
    print("type help for list of options")
    main()
