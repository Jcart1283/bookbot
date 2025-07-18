from stats import num_words
from stats import character_count
from stats import character_sort
from sys import argv# as argv

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
#    print("runing main")
#    print(len(argv))
    if len (argv) !=2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    try:
#        print(argv[1])
        book_source = argv[1]
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
    except Exception as e:
        print(f'ERROR:{e}')
        return e

#print(argv)

if __name__ == "__main__":  
    main()
elif argv[0] == 'main.py':
    main()