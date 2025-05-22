words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
current_word_index = 0
answer = []
last_line = False
while current_word_index < len(words):
    row_chars = ""
    number_of_words_in_row = 1
    current_len = len(words[current_word_index])
    for i in range(len(words) - current_word_index):
        if current_word_index + 1 == len(words):
            last_line = True
            break
        if current_len + 1 + len(words[current_word_index + 1]) <= maxWidth:
            current_len += 1 + len(words[current_word_index  + 1])
            number_of_words_in_row += 1
        else:
            break
        current_word_index += 1
    if last_line:
        for i in range(number_of_words_in_row - 1):
            row_chars += words[current_word_index - number_of_words_in_row + 1 + i]
            row_chars += ' '
        row_chars += words[current_word_index]
        row_chars += ' ' * (maxWidth - len(row_chars))
        answer.append(row_chars)
        break
    spaces = []
    spaces_available = maxWidth-(current_len - (number_of_words_in_row - 1))
    spaces_left = spaces_available
    for i in range(number_of_words_in_row - 1):
        spaces.append(spaces_available// (number_of_words_in_row - 1))
        spaces_left -= spaces_available// (number_of_words_in_row - 1)
    for i in range(number_of_words_in_row - 1):
        if spaces_left > 0:
            spaces[i] += 1
            spaces_left -= 1
        else:
            break
    for i in range(number_of_words_in_row - 1):
        row_chars += words[current_word_index - number_of_words_in_row + 1 + i]
        row_chars += ' ' * spaces[i]
    row_chars += words[current_word_index]
    if number_of_words_in_row == 1:
        row_chars += ' ' * (maxWidth - len(row_chars))
    answer.append(row_chars)
    current_word_index += 1

print(answer)