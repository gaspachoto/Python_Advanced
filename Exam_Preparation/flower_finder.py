from collections import deque


def letter_found(vowel, consonant, word_dict):
    result = False
    if vowel in word_dict:
        word_dict[vowel] = True
        result = True
    if consonant in word_dict:
        word_dict[consonant] = True
        result = True

    return result


vowels = deque(input().split())
consonants = input().split()
rose = {letter: False for letter in "rose"}
tulip = {letter: False for letter in "tulip"}
lotus = {letter: False for letter in "lotus"}
daffodil = {letter: False for letter in "daffodil"}
word_found = None

while vowels and consonants:
    vowel_letter = vowels.popleft()
    consonant_letter = consonants.pop()

    if letter_found(vowel_letter, consonant_letter, rose):
        if all(rose.values()):
            word_found = 'rose'
            break
    if letter_found(vowel_letter, consonant_letter, tulip):
        if all(tulip.values()):
            word_found = 'tulip'
            break
    if letter_found(vowel_letter, consonant_letter, lotus):
        if all(lotus.values()):
            word_found = 'lotus'
            break
    if letter_found(vowel_letter, consonant_letter, daffodil):
        if all(daffodil.values()):
            word_found = 'daffodil'
            break

if word_found:
    print(f"Word found: {word_found}")
else:
    print(f"Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
