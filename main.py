#book bot main
from stats import word_count, char_count, report
import sys
#"./books/frankenstein.txt

def get_book_text(path):
    with open(path) as f:
        content = f.read()
        return content

def main():

    if (len(sys.argv)!=2):
        print("incorrect params")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path=sys.argv[1]
    wc=word_count(get_book_text(path))
    charCount=char_count(get_book_text(path))
    print(f"Found {wc} total words")
    sorted=report(charCount)

    for s in sorted:
        if(s["char"].isalpha()):
            print(f"{s["char"]}: {s["num"]}")



main()

