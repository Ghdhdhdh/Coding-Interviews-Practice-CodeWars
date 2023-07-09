def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = load_words()

for word in words:
    wordWithoutFirstLetter = word[1:]
    firstLetter = word[0]
    for letter in letters:
        if letter == firstLetter:
            continue
        if str(letter) + str(wordWithoutFirstLetter) in words:
            print(f"If you remove {word[0]} from {word} and add {letter} you get {str(letter) + str(wordWithoutFirstLetter)}")
