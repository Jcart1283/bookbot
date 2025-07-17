from stats import num_words
from stats import character_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_text = get_book_text('books/frankenstein.txt')
    wordcount = num_words(book_text)
    print(f'{wordcount} words found in the document')
    print(character_count(book_text))



if __name__ == "__main__":  
    main()
