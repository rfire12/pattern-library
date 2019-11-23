from pattern.es import singularize, pluralize, tag, parse, parsetree, pprint, PAST, predicative, FEMALE, PLURAL, conjugate, INFINITIVE, attributive

def pluralize_singularize():
    print(pluralize('gato'))
    print(singularize('gatos'))

# Verb conjugation
def verb_conjugation():
    print(conjugate('Soy', INFINITIVE))
    print(conjugate('Soy', PAST))

#Adjetives
def adjetives():
    print(predicative('hermosos'))
    print(attributive('hermoso', gender=FEMALE+PLURAL))

# Grammatical tagging
def grammatical_tagging():
    sentence = "El perro negro muerde sin parar."
    print(tag(sentence))
    pprint(parse(sentence))

#pluralize_singularize()
#verb_conjugation()
#adjetives()
#grammatical_tagging()