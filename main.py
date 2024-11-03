import re

writing_path = 'writing.txt'
word_path = 'word.csv'


with open(word_path, 'r', encoding='utf-8') as word_f:
    word_list = word_f.read().split(',')


with open(writing_path, 'r', encoding='utf-8') as writing_f:
    text = writing_f.read()


found_words = []

for word in word_list:
    if re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE):
        found_words.append(word)


print(f"확인된 단어: {found_words}")