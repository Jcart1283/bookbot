def num_words(book_text):
    return len(book_text.split())

def character_count(book_text):
    count = {}
    lowered = book_text.lower()
    letters = list(lowered)
    for l in letters:
        if l in count:
            count[l]+=1
        else:
            count[l] = 1
    return count
