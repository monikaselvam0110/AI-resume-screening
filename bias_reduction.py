import re

def anonymize_text(text):
    text = re.sub(r"\b(male|female)\b", "", text)
    text = re.sub(r"\b\d{2}\b", "", text)   # age removal
    text = re.sub(r"\b(name|gender|dob)\b", "", text)
    return text
