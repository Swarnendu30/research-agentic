import pytest
from agents.research_agent import collect_data
from agents.answer_agent import draft_answer
from agents.fact_checker_agent import fact_check
from agents.citation_agent import generate_citations

def test_collect_data():
    query = "Latest AI trends"
    results = collect_data(query)
    assert isinstance(results, str)
    assert len(results) > 0

def test_draft_answer():
    context = "AI is evolving rapidly with new models."
    answer = draft_answer(context)
    assert isinstance(answer, str)
    assert len(answer) > 0

def test_fact_check():
    context = "AI will end humanity next week."
    checked = fact_check(context)
    assert isinstance(checked, str)
    assert "true" in checked.lower() or "false" in checked.lower()

def test_generate_citations():
    query = "Artificial Intelligence"
    citations = generate_citations(query)
    assert isinstance(citations, list)
