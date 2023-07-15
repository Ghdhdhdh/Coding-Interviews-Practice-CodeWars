def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

words = load_words()

word_to_rhyme_with = "hello"

for word in words:
	for i in range(len(word)):
		ending = word[i:]
		try:
			if ending == word_to_rhyme_with[len(ending) * -1]:
				print(f"{word} rhymes with {word_to_rhyme_with}")
		except IndexError:
			pass