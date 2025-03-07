import streamlit as st
from chains.processing_chain import processing_chain
from utils.pdf_exporter import generate_pdf

def launch_gui():
    st.set_page_config(
        page_title="Deep Research Agentic System",
        page_icon="🧠",
        layout="wide",
    )

    st.markdown("""
        <style>
        body { background-color: #000000; }
        .stApp { background-color: #000000; color: #FFD700; }
        h1, h2, h3, h4 { color: #FFD700; }
        .stButton>button { background-color: #FF1493; color: white; border-radius: 12px; padding: 0.5em 1em; font-weight: bold; }
        .stTextInput>div>div>input { background-color: #222; color: #FFD700; }
        .stSpinner>div>div { color: #FF1493; }
        </style>
    """, unsafe_allow_html=True)

    st.title("🧠 Deep Research Agentic System")

    query = st.text_input("Enter your research question:")

    if st.button("🚀 Run Full Research"):
        if not query.strip():
            st.error("Please enter a research question.")
        else:
            with st.spinner('🔍 Running full research with LangGraph...'):
                result = processing_chain(query)

            answer = result.get("answer", "No answer generated.")
            citations = result.get("citations", [])

            st.subheader("📝 Final Answer")
            st.success(answer)

            st.subheader("🔗 Citations")
            for citation in citations:
                st.markdown(f"- {citation}")

            pdf_file = generate_pdf(answer, citations)

            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="⬇️ Download Full Report (PDF)",
                    data=f,
                    file_name="research_report.pdf",
                    mime="application/pdf",
                    help="Download your full research report with answer and sources.",
                )
