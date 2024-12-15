# text = ('this is sample text with several words this is more sample text with some different words')

# word_count={}
# for words in text.split():
#     if words in word_count:
#         word_count[words] += 1
#     else:
#         word_count[words] = 1

# for wd, ct in sorted(word_count.items()):
#     print(f'{wd}: {ct}')



# using Counter
from collections import Counter
text = ('this is sample text with several words this is more sample text with some different words')

count = Counter(text.split())
print(count)
# Counter({'this': 2, 'is': 2, 'sample': 2, 'text': 2, 'with': 2, 'words': 2, 'several': 1, 'more': 1, 'some': 1, 'different': 1})
for wd, ct in sorted(count.items()):
    print(f'{wd}: {ct}')