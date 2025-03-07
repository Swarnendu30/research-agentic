# utils/data_cleaner.py

import re

def clean_text(text):
    """Clean up the raw text from Tavily."""
    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()
    # Optional: Remove non-ASCII chars
    text = text.encode("ascii", errors="ignore").decode()
    return text

def deduplicate_texts(text_list):
    """Remove duplicate entries from a list of texts."""
    return list(dict.fromkeys(text_list))
