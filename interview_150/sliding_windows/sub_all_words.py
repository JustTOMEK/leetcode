from collections import Counter
s = "barfoothefoobarman"
words = ["foo","bar"]
word_len = len(words[0])
len_s = len(s)
number_of_words = len(words)
output = []
og_dictionary = {}
for word in words:
    if word not in og_dictionary:
        og_dictionary[word] = 1
    else:
        og_dictionary[word] += 1

for l in range(0, len_s - word_len * number_of_words + 1):
    current_set_len = number_of_words
    current_dictionary = {}
    for j in range(l, l + word_len * number_of_words, word_len):
        word = s[j:j + word_len]
        if word in og_dictionary:
            if word in current_dictionary:
                current_dictionary[word] += 1
            else:
                current_dictionary[word] = 1
            if current_dictionary[word] > og_dictionary[word]:
                break
        else:
            break
    else:
        output.append(l)

print(output)