#book bot main
from stats import word_count, char_count

def get_book_text(path):
    with open(path) as f:
        content = f.read()
        return content

def main():
    wc=word_count(get_book_text("./books/frankenstein.txt"))
    charCount=char_count(get_book_text("./books/frankenstein.txt"))
    print(f"{wc} words found in the document")
    print(charCount)



main()

