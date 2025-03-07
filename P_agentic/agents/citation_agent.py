from datetime import datetime
from urllib.parse import urlparse


def extract_domain(url):
    """Pulls the domain to use as the source if no better option."""
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace("www.", "")
        return domain.capitalize()
    except:
        return "Unknown Source"


def extract_year(date_str):
    """Extracts the year from a date string, if possible."""
    try:
        return datetime.fromisoformat(date_str).year
    except:
        return "n.d."


def generate_citations(sources):
    """
    Generate APA-style citations from provided sources without filtering.
    """
    citations = []
    for res in sources:
        title = res.get("title", "No title").rstrip(".")
        url = res.get("url", "[URL not available]")
        source = res.get("source") or extract_domain(url)
        year = extract_year(res.get("published_date", ""))

        citation = f"{source}. ({year}). {title}. Retrieved from {url}"
        citations.append(citation)

    return citations if citations else ["No valid citations found."]
