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

def sort_on(item):
    return item["num"]

def character_sort(char_dict):
    output_list = [{"char": c, "num": n} for c, n in char_dict.items()]
    output_list.sort(reverse=True, key=sort_on)
#   output_list = [f'"char" : "{c}", "num" : "{char_dict[c]}"']
#    for c in char_dict:
#        output_dict.append(f'"char" : "{c}", "num" : "{char_dict[c]}"')
    return output_list
