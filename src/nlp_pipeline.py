import spacy
#Loads an NLP library that can understand text, detect names, places, organizations
nlp = spacy.load("en_core_web_sm") #This loads a pre-trained English language model

def extract_entities(text):
    doc = nlp(text)
    #spaCy reads full text and converts it into: tokens (words), meaning entity detection

    entities = {
        "PERSON": [],
        "ORG": [],
        "GPE": [],   # countries, cities
        "MONEY": []
    }

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    return entities