from pattern.web import Google, Twitter
from pattern.vector import words, count, stem, PORTER, LEMMA
from pattern.en import singularize, pluralize, tag, parse, parsetree, pprint, suggest, sentiment,


# Google
def google_search():
    g = Google()
    for r in g.search(query="Barcamp RD 2019", star=1,count=10):
        print(r.title, r.text, r.url)

# Twitter
def twitter_search():
    t = Twitter(language='es')
    i = None
    for j in range(3): # For pagination
        for r in t.search(query="#DonaldTrump", start=i, count=10):
            print(r.id, r.text, r.date)
        i = r.id
        print("----------------@@@@@@-------------")



# Tokenization

def tokenization():
    text = "My new car is better than my new bed"
    tokens = words(text)
    print(tokens)
    print(count(tokens))


# Roots and lemmas

def roots_and_lemmas():
    
    print(stem('cars', PORTER)) #Root
    print(stem('cars', LEMMA))
    print(stem('studies', PORTER)) # Root
    print(stem('studies', LEMMA))

    text = "People who teach find teaching very rewarding."
    tokens = words(text)
    print(count(tokens, stopwords=True, stemmer=PORTER))
    print(count(tokens, stopwords=True, stemmer=LEMMA))


# Pluralize and sigularize

def pluralize_and_sigularize():
    print(singularize('cats'))
    print(pluralize('the house'))


# Grammatical tagging
def grammatical_tagging():
    sentence = "The white house is at the top of the hill"
    sentences = "The white house is at the top of the hill. My house is not"

    print(tag(sentence)) # The result is an array of tuples tagging each word (verbs, nouns, etc.) 
    print(parse(sentence))
    #pprint(parse(sentence))

    pprint(parsetree(sentences))
# 

# Spell checker

def spell_checker():
    print(suggest('poblem'))



# Feelings

def feelings():
    review = "I love my iphone :-D"
    sent = sentiment(review)
    print(sent) # It returns (sentiment score) and (subjective rate)
    print(sent.assessments) # It returns the words that sentiment used to calculate the score
    # Lower - Negative      Higher - Positive

#google_search()
#twitter_search()
#tokenization()
#roots_and_lemmas()
#pluralize_and_sigularize()
#grammatical_tagging()
#spell_checker()
feelings()