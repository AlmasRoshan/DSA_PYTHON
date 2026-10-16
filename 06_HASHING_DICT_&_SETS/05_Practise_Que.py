# PRACTISE QUESTIONS

def first_repeated(items):
    new_arr = set()
    for item in items:
        if item in new_arr:
            return item # returns the item that is repeated in the list
        else:
            new_arr.add(item)
    return None # returns None if item is not repeated
print(first_repeated([3, 1, 4, 1, 5]))  # 1


def repeated(sentence):
    freq = {}
    for ch in sentence.split():
        freq[ch] = freq.get(ch, 0) + 1
    return max(freq, key=freq.get)
print(repeated("chai garam chai thanda chai"))    # chai