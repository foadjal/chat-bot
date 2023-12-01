import spacy

def preprocess_input(input_text, nlp):
    """
    Effectue le prétraitement du texte d'entrée en utilisant spaCy.
    Retourne le document spaCy.
    """
    doc = nlp(input_text)
    return doc

def extract_entities(doc):
    """
    Extrait les entités du document spaCy.
    Retourne une liste d'entités.
    """
    return [ent.text for ent in doc.ents]

def extract_nouns(doc):
    """
    Extrait les noms du document spaCy.
    Retourne une liste de noms.
    """
    return [token.text for token in doc if token.pos_ == "NOUN"]

def extract_verbs(doc):
    """
    Extrait les verbes du document spaCy.
    Retourne une liste de verbes.
    """
    return [token.text for token in doc if token.pos_ == "VERB"]
