from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize as wt, sent_tokenize

def to_lower_case(txt):
    return txt.lower()

def remove_stop_words(words):
    return [word for word in words if word not in stopwords.words('english')]

def word_tokenize(txt):
    return wt(txt)

def sentence_tokenize(txt):
    return sent_tokenize(txt)

def stem_tokens(tokens):
    return [PorterStemmer().stem(t) for t in tokens]