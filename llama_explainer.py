import subprocess

def explain(summary_text):
    prompt = f"""
You are a data quality expert.
Analyze the following data summary and explain the main issues in simple language.

SUMMARY:
{summary_text}
"""

    result = subprocess.run(
        ["ollama", "run", "llama3.2:3b"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()


if __name__ == "__main__":
    test_summary = """
Total rows: 100
Invalid emails: 23
Duplicate rows: 15
Missing company names: 12
"""
    explanation = explain(test_summary)
    print("AI EXPLANATION:")
    print(explanation)
