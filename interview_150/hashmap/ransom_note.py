ransomNote = "aa"
magazine = "aab"

dict = {}
for letter in magazine:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 0

for letter in ransomNote:
    if letter in dict:
        if dict[letter] == 0:
            print(False)
        dict[letter] -= 1
    else:
        print(False)