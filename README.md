# Private Data Intelligence Engine (PDIE)

A privacy-first, local AI application that validates CSV data quality and explains issues in plain language — without sending data to the cloud.

<img width="900" height="461" alt="image" src="https://github.com/user-attachments/assets/80179af1-66d4-4754-983e-5438f4a6ced7" />


## What it does
- Upload a CSV file via a simple web UI
- Runs deterministic data checks (emails, duplicates, missing fields)
- Uses **LLaMA 3 via Ollama (local)** to generate human-readable explanations
- No APIs, no external calls, no data leaves the machine

## Why it matters
Most data quality tools require cloud uploads or technical expertise.  
PDIE is designed for **non-technical users** who need fast, explainable insights while keeping data private.

## Tech Stack
- Python
- Streamlit (UI)
- Ollama (local LLM runtime)
- LLaMA 3
- Rule-based validation + AI explanation layer

## Architecture
Streamlit UI
↓
Rule-based Validation Engine
↓
Local LLM (LLaMA 3 via Ollama)

## How to run locally
```bash
pip install streamlit
python -m streamlit run app.py

## How to run locally
```bash
pip install streamlit
python -m streamlit run app.py
Runs fully offline once dependencies are installed.

Example Use Cases

Marketing lead list validation

CRM data hygiene checks

Sales ops CSV audits

Privacy-sensitive datasets

Privacy

No cloud APIs

No tracking

**## Security & Privacy
- Runs entirely on localhost
- No external API calls
- No credentials required
- No data persistence
- Designed for privacy-sensitive datasets


No data storage**

Runs entirely on localhost



