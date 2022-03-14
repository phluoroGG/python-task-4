def read_string_from_file(filename):
    file = open(filename, 'r', encoding='utf-8')
    string = file.read()
    file.close()
    return string


def reverse_words_symmetrical(string):
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    chars = list(string)
    for j in range(len(chars)):
        char = chars[j]
        if english_alphabet.find(char.lower()) + 1:
            chars[j] = english_alphabet[len(english_alphabet) - english_alphabet.find(char.lower()) - 1]
            if char.isupper():
                chars[j] = chars[j].upper()
        elif russian_alphabet.find(char.lower()) + 1:
            chars[j] = russian_alphabet[len(russian_alphabet) - russian_alphabet.find(char.lower()) - 1]
            if char.isupper():
                chars[j] = chars[j].upper()
    return ''.join(chars)


if __name__ == '__main__':
    filename_ = "input01.txt"
    reversed_string = reverse_words_symmetrical(read_string_from_file(filename_))
    print(reversed_string)
    print(reverse_words_symmetrical(reversed_string))
