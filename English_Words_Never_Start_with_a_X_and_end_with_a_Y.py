def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

words = load_words()


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
combos = []
for startingletter in letters:
    for endingletter in letters:
        combos.append([startingletter, endingletter])

for word in words:
    try:
        combos.remove([word[0], word[len(word) - 1]])
    except ValueError:
        pass


for combo in combos:
    print(f"No word will ever start with {combo[0]} and end with {combo[1]}")



