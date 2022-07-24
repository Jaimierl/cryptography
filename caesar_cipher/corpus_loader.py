# natural language toolkit (nltk)- a library you need to do a pip install on.

import ssl
# Need this to pull in the info from the nltk to help connect to the library
import nltk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

print(word_list)
