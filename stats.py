def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_char_count(book_text):
    char_counts = {}
    
    for char in book_text:
        char = char.lower()
       
        if char in char_counts:
            char_counts[char] +=1
        else:
            char_counts[char] = 1
    
    return char_counts
       
def sort_on(item):
    return item["num"]

def sort_char_counts(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        sorted_list.append({
            "char": char,
            "num": count
        })

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

