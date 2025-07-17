from stats import num_words
from stats import character_count
from stats import character_sort

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_source ='books/frankenstein.txt'
    book_text = get_book_text(book_source)
    wordcount = num_words(book_text)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_source}...')
    print("----------- Word Count ----------")
    print(f'Found {wordcount} total words')
    print("--------- Character Count -------")
    character_count_list = (character_sort(character_count(book_text)))
    for i in character_count_list:
        print(f'{i["char"]}: {i["num"]}')



if __name__ == "__main__":  
    main()
