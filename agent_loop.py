import os
import re
from datetime import datetime

from agents.planner_agent import create_plan
from agents.executor_agent import execute_plan
from agents.research_agent import ask_llm
from memory.conversation_memory import Memory


# ✅ Safer folder naming (Windows + Linux safe)
def safe_folder_name(text):
    text = re.sub(r'[<>:"/\\|?*]', '', text)
    text = re.sub(r'\s+', '_', text)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{text}_{timestamp}"


# ✅ Main Autonomous Pipeline
def autonomous_research(topic):

    try:
        folder = os.path.join("papers", safe_folder_name(topic))
        os.makedirs(folder, exist_ok=True)

        memory = Memory()

        print("\n🧠 Creating research plan...\n")

        # 🔥 STEP 1 — Planner
        plan = create_plan(topic)

        print("===== RESEARCH PLAN =====\n")
        print(plan)

        print("\n🔎 Executing research...\n")

        # 🔥 STEP 2 — Executor (search + PDFs)
        results, pdfs = execute_plan(topic, folder)

        print("📚 Sources collected:", len(results))
        print("📄 PDFs downloaded:", len(pdfs))

        print("\n✍️ Generating research report...\n")

        # 🔥 STEP 3 — Synthesized Report
        summary_prompt = f"""
        You are an expert research analyst.

        Follow this research plan:

        {plan}

        Now write a HIGH-QUALITY research report on:

        {topic}

        Requirements:
        - Academic tone
        - Structured format
        - Cite insights from multiple sources
        - Avoid generic explanations

        Include sections:

        ✅ Executive Summary  
        ✅ Key Concepts  
        ✅ Scientific / Technical Foundations  
        ✅ Recent Advancements  
        ✅ Challenges  
        ✅ Future Research Directions  
        """

        report = ask_llm(summary_prompt, memory)

        return report, pdfs

    except Exception as e:
        print("\n🚨 ERROR in autonomous pipeline:")
        print(str(e))
        return None, []


# ✅ CLI Entry
if __name__ == "__main__":

    print("\n==============================")
    print("🔬 Autonomous Research Agent")
    print("==============================\n")

    topic = input("Enter research topic: ")

    result, files = autonomous_research(topic)

    if result:
        print("\n===== FINAL RESEARCH REPORT =====\n")
        print(result)

    if files:
        print("\nDownloaded PDFs:")
        for f in files:
            print("✔", f)
