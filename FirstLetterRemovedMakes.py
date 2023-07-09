def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

words = load_words()

for word in words:
    if word[1:] in words:
        print(f"if you remove {word[0]} from {word} you get {word[1:]}")