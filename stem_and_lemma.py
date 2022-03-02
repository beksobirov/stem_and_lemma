# 1st method import nltk
# import nltk
# wn = nltk.WordNetLemmatizer()
# ps = nltk.PorterStemmer()
# End 1st method

# 2nd method import nltk
from nltk import WordNetLemmatizer, PorterStemmer
wn = WordNetLemmatizer()
ps = PorterStemmer()
# End 2nd method

#dir(wn)
#dir(ps)

print(ps.stem('goose')) #goos
print(ps.stem('geese')) #gees

print(wn.lemmatize('goose')) #goose
print(wn.lemmatize('geese')) #goose

print(wn.lemmatize('better'))          #better
print(wn.lemmatize('better', pos='a')) #good
