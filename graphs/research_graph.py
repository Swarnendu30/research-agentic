from langgraph.graph import StateGraph, END
from agents.research_agent import collect_data
from agents.fact_checker_agent import fact_check
from agents.answer_agent import draft_answer
from agents.citation_agent import generate_citations
from utils.data_cleaner import clean_text


class ResearchState:
    def __init__(self, query, context="", facts_verified=False, quality_score=0, final_answer="", citations=""):
        self.query = query
        self.context = context
        self.facts_verified = facts_verified
        self.quality_score = quality_score
        self.final_answer = final_answer
        self.citations = citations


def research_node(state: ResearchState):
    state.context = collect_data(state.query)
    state.context = clean_text(state.context)
    return state


def parallel_fact_check_node(state: ResearchState):
    verified_context = fact_check(state.context)
    state.context = verified_context
    state.facts_verified = True  
    return state


def drafting_node(state: ResearchState):
    state.final_answer, state.quality_score = draft_answer(state.context)
    return state


def quality_check(state: ResearchState):
    return state.quality_score >= 8  


def citation_node(state: ResearchState):
    state.citations = generate_citations(state.query)
    return state


def build_research_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("research", research_node)
    graph.add_node("fact_check", parallel_fact_check_node)
    graph.add_node("draft", drafting_node)
    graph.add_node("citations", citation_node)

    graph.set_entry_point("research")
    graph.add_edge("research", "fact_check")
    graph.add_edge("fact_check", "draft")
    
    graph.add_conditional_edges(
        "draft",
        quality_check,
        {
            True: "citations",
            False: "research",  
        },
    )

    graph.add_edge("citations", END)

    return graph.compile()
