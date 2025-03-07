# chains/processing_chain.py

from agents.research_agent import collect_data
from agents.fact_checker_agent import fact_check
from agents.answer_agent import draft_answer
from agents.citation_agent import generate_citations


def processing_chain(query):
    """
    Orchestrates the complete research workflow:
    1. Collect data and sources.
    2. Fact-check the data.
    3. Draft an answer.
    4. Generate citations from original sources.
    """
    # Step 1: Collect raw data and sources
    research_context, sources = collect_data(query)

    # Step 2: Fact-check the collected data
    verified_context = fact_check(research_context)

    # Step 3: Draft a well-structured answer
    answer = draft_answer(verified_context)

    # Step 4: Format proper citations from the actual sources
    citations = generate_citations(sources)

    return {
        "query": query,
        "context": verified_context,
        "answer": answer,
        "citations": citations
    }
