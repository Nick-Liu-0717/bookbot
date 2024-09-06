def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_of_words = get_num_words(text)
    print(f"{num_of_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()  

main()