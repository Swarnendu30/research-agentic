import re

def clean_text(text):
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = text.encode("ascii", errors="ignore").decode()
    return text

def deduplicate_texts(text_list):
    return list(dict.fromkeys(text_list))
