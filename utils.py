import re

def clean_text(text):
    """
    Nettoie le texte en supprimant les caractères spéciaux et en le mettant en minuscules.
    """
    cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return cleaned_text.lower()

def tokenize_text(text):
    """
    Tokenize le texte en séparant les mots.
    """
    return text.split()

def remove_stopwords(words, stopwords):
    """
    Supprime les mots vides (stopwords) d'une liste de mots.
    """
    return [word for word in words if word not in stopwords]

# Vous pouvez ajouter d'autres fonctions utilitaires selon vos besoins
