#A
#number of words
def words_number(text):
    if text[0] != ' ': 
        count = 1
    else:
        count = 0
    for i in range(len(text)-1):
        if text[i] != ' ' and text[i+1] == ' ': count += 1
    return count

def words_number_by_split(text):
    return len(text.split())

#B
#array of words ordered by length
def order_by_length(text):
    word = text.split()
    for i in range(len(word)):
        length = len(word[i])
        max = i
        for j in range(i+1,len(word)):
            if len(word[j]) > length: 
                max = j
                length = len(word[max])
        word[i], word[max] = word[max], word[i]
    return word

#C
#sort words alphabetically
def sort_alpha(text):
    return sorted(text.split(), key=str.casefold)
