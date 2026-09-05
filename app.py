import streamlit as st
from agents.planner_agent import create_plan
from agents.research_agent import ask_llm
from tools.web_search import search_web


# ---------------- CONFIG ---------------- #

st.set_page_config(
    page_title="Deep Research Agent",
    page_icon="🧠",
    layout="wide"
)


# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("🧠 Deep Research Agent")

    st.markdown("""
### ⚡ Agent Capabilities
- Autonomous planning  
- Multi-source research  
- Local LLM reasoning  
- Structured report generation  
""")

    st.divider()

    st.success("✅ Running Fully Local\nNo API Costs")

    st.divider()

    st.markdown("Built for serious research workflows.")


# ---------------- HEADER ---------------- #

st.title("🚀 Deep Autonomous Research Agent")

st.markdown("""
Ask a complex research question.

The agent will:

🧠 Plan the research  
🔎 Search the web  
📚 Analyze sources  
✍️ Generate a structured report  
""")

st.divider()


# ---------------- INPUT ---------------- #

query = st.text_input(
    "Enter a research topic:",
    placeholder="Example: Biological mechanisms of protein digestion"
)


# ---------------- RUN ---------------- #

if st.button("Run Autonomous Research", use_container_width=True):

    if not query:
        st.warning("Please enter a research topic.")
        st.stop()

    # -------- STEP 1: PLAN -------- #

    with st.spinner("🧠 Creating research plan..."):
        plan = create_plan(query)

    st.subheader("🧠 Research Plan")
    st.info(plan)

    # -------- STEP 2: SEARCH -------- #

    with st.spinner("🔎 Searching academic sources..."):
        results = search_web(query)

    st.subheader("📚 Sources Identified")

    for r in results[:5]:
        st.markdown(f"- [{r['title']}]({r['url']})")

    # -------- STEP 3: REPORT -------- #

    with st.spinner("✍️ Writing research report..."):

        sources = "\n".join([r["title"] for r in results])

        prompt = f"""
        You are an expert research analyst.

        Follow this research plan:

        {plan}

        Topic:
        {query}

        Sources:
        {sources}

        Write a HIGH-quality research report with:

        - Executive Summary
        - Key Concepts
        - Scientific Foundations
        - Recent Advancements
        - Challenges
        - Future Directions
        """

        report = ask_llm(prompt)

    st.success("✅ Research Complete")

    st.subheader("📄 Final Research Report")
    st.write(report)
