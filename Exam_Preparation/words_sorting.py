def words_sorting(*args):
    def calculate_word_value(word):
        return sum(ord(x) for x in word)

    word_dict = {word: calculate_word_value(word) for word in args}
    total_words_value = sum(word_dict.values())
    if total_words_value % 2 == 0:
        result = sorted(word_dict.items())
    else:
        result = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    return '\n'.join(f'{word} - {count}' for (word, count) in result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
