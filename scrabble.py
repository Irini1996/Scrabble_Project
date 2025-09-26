# https://github.com/jmlewis/valett/blob/master/scrabble/sowpods.txt
# TABIND Scrabble 
# The objective of this project is to develop a program that takes the letter combination “tabind” only once and creates an alphabetical list of all the words, from a Scrabble dictionary that can be found with those letters. 

from collections import Counter

letters = "tabind"  # the letters we want to use
bag = Counter(letters)


with open("dict.txt", "r", encoding="utf-8") as f:
    words = [w.strip().lower() for w in f if w.strip()]

# Keep only words that:
# i) are at least 2 letters long
# ii) can be formed with the available letters in bag
valid = [w for w in words if len(w) >= 2 and not (Counter(w) - bag)]


# Sort valid words alphabetically
valid.sort()

print(f"Found {len(valid)} words with the letters '{letters}':\n")
for w in valid:

    print(w)
