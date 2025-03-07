import pytest
from graphs.research_graph import build_research_graph

def test_research_workflow():
    query = "What is LangGraph?"
    result = build_research_graph(query)
    assert isinstance(result, dict)
    assert "answer" in result
    assert "citations" in result
    assert len(result["answer"]) > 0
