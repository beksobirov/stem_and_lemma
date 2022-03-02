import nltk
wn = nltk.WordNetLemmatizer()
ps = nltk.PorterStemmer()

#dir(wn)
#dir(ps)

print(ps.stem('goose')) #goos
print(ps.stem('geese')) #gees

print(wn.lemmatize('goose')) #goose
print(wn.lemmatize('geese')) #goose

print(wn.lemmatize('better'))          #better
print(wn.lemmatize('better', pos='a')) #good
