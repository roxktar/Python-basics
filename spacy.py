import spacy 

nlp = spacy.load('en')
doc=nlp("Galgotias University is a private university on Yamuna Expressway in Dankaur, Uttar Pradesh, India. Established in 2011 ")
for token in doc:
    print(token)