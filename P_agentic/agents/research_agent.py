# agents/research_agent.py
from utils.data_cleaner import clean_text, deduplicate_texts
from tavily import TavilyClient
from configs.settings import TAVILY_API_KEY

def collect_data(query):
    """
    Uses Tavily API to collect research data and sources.
    """
    tavily = TavilyClient(api_key=TAVILY_API_KEY)
    
    response = tavily.search(
        query=query,
        search_depth="advanced",  # Use "basic" or "advanced"
        include_answers=True,
        include_images=False,
        max_results=10
    )
    
    # Extract and clean the contents
    results = [clean_text(result["content"]) for result in response["results"]]
    results = deduplicate_texts(results)

    # Combine all the cleaned, deduplicated results into one string
    combined_results = "\n\n".join(results)
    
    # Return both the context and the raw sources
    return combined_results, response["results"]
