def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersdic= {}
temp_word = ""
words = load_words()

for letter in letters:
    lettersdic[letter] = 0
    
lettersdic["starter"] = 0

for word in words:
    wordlen = len(word)
    for i in range(wordlen):
        lettersdic[word[i-1]] = lettersdic[word[i-1]] + 1
        
        
most_used_letter = "starter"
for k, v in lettersdic:
    if v > lettersdic[most_used_letter]:
        most_used_letter = v
        
print(f"The Most Used Letter In The English Alphabet is {most_used_letter}")


