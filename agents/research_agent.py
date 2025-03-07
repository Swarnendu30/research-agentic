from utils.data_cleaner import clean_text, deduplicate_texts
from tavily import TavilyClient
from configs.settings import TAVILY_API_KEY

def collect_data(query):

    tavily = TavilyClient(api_key=TAVILY_API_KEY)
    
    response = tavily.search(
        query=query,
        search_depth="advanced",  
        include_answers=True,
        include_images=False,
        max_results=10
    )
    
    results = [clean_text(result["content"]) for result in response["results"]]
    results = deduplicate_texts(results)

    combined_results = "\n\n".join(results)
    
    return combined_results, response["results"]
