import re
from collections import Counter
def word_frequency(text):
    words=re.findall(r'\b\w+\b',text.lower())
    frequency=Counter(words)
    return list(frequency.items())
text="the cat and the dog"
result=word_frequency(text)
print(result)