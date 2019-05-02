import re
import collections

text = open('files/book.txt', encoding="utf8").read().lower()
# \w+ = \w not a whitespace, + one for more
words = re.findall("\w+", text)
print(collections.Counter(words).most_common(10))