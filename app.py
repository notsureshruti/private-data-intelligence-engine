import streamlit as st
import csv
from ai.llama_explainer import explain

st.set_page_config(page_title="Private Data Intelligence Engine", layout="centered")

st.title("📊 Private Data Intelligence Engine")
st.write("Upload a CSV file to validate data quality and get an AI explanation (runs locally).")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

def is_valid_email(email):
    return "@" in email and "." in email

if uploaded_file is not None:
    reader = csv.DictReader(uploaded_file.read().decode("utf-8").splitlines())
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

    st.subheader("🔍 Data Quality Summary")

    col1, col2 = st.columns(2)
    col1.metric("Total rows", len(rows))
    col2.metric("Invalid emails", invalid_emails)

    col3, col4 = st.columns(2)
    col3.metric("Duplicate rows", duplicate_rows)
    col4.metric("Missing company names", missing_company_names)

    summary = f"""
    Total rows: {len(rows)}
    Invalid emails: {invalid_emails}
    Duplicate rows: {duplicate_rows}
    Missing company names: {missing_company_names}
    """

    with st.spinner("Running local AI explanation..."):
        ai_explanation = explain(summary)

    st.subheader("🧠 AI Explanation")
    st.write(ai_explanation)
