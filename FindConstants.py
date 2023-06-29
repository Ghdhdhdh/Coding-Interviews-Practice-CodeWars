def consonant_count(s):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    count = 0
    for letter in s:
        if letter.lower() in consonants:
            print(letter + " is NOT a Vowel")
            count += 1
        else:
            print(letter + " is A Vowel")
    return count