from ai.llama_explainer import explain
import csv

def is_valid_email(email):
    return "@" in email and "." in email

with open("data/sample.csv", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

invalid_emails = 0
seen_emails = set()
duplicate_rows = 0
missing_company_names = 0

for row in rows:
    email = row.get("email", "").strip()
    company = row.get("company_name", "").strip()

    if not is_valid_email(email):
        invalid_emails += 1

    if email in seen_emails:
        duplicate_rows += 1
    else:
        seen_emails.add(email)

    if company == "":
        missing_company_names += 1

summary = f"""
Total rows: {len(rows)}
Invalid emails: {invalid_emails}
Duplicate rows: {duplicate_rows}
Missing company names: {missing_company_names}
"""

print(summary)

ai_explanation = explain(summary)
print("\nAI EXPLANATION:\n")
print(ai_explanation)
