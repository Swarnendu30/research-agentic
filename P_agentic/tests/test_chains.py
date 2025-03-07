import pytest
from chains.processing_chain import run_processing_chain

def test_run_processing_chain():
    query = "Impact of quantum computing"
    result = run_processing_chain(query)
    assert isinstance(result, dict)
    assert "answer" in result
    assert "citations" in result
    assert len(result["answer"]) > 0
