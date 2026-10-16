# FREQUENCY COUNTING

# CHARACTER FREQUENCY COUNTING
def char_frequency_count(string):
    freq = {}
    for ch in string:
        freq[ch] = freq.get(ch, 0) + 1  # Increment the count for the character
    return freq
print(char_frequency_count("banana"))  # Output: {'b': 1, 'a': 3, 'n': 2}

# WORD FREQUENCY COUNTING
def word_frequency_count(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1  # Increment the count for the word
    return freq
print(word_frequency_count("chai garam chai garam chai"))  # Output: {'chai': 3, 'garam': 2}

