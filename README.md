# Green Prompt - Real-Time Carbon Footprint Estimator for Sustainable AI Usage

## Problem Statement

Organizations integrating Large Language Models (LLMs) into their workflows often lack visibility into the environmental impact of AI usage.

This project provides:

* Real-time carbon footprint estimation
* AI sustainability monitoring
* Production log analysis
* Executive summaries
* Optimization recommendations

The goal is to help enterprises reduce AI-related carbon emissions while maintaining productivity.

---

# Features

## Step 1 - User Interaction

Accepts user questions regarding:

* AI Sustainability
* Carbon Emissions
* Green AI
* LLM Usage
* CO2 Reporting

Example:

```text
What is today's carbon footprint?
```

---

## Step 2 - Domain Expert Restriction

The application acts as a sustainability domain expert.

Allowed Topics:

* Carbon Footprint
* CO2 Emissions
* Sustainable AI
* Green Computing
* AI Energy Consumption

Rejected Topics:

```text
Who won IPL?
```

```text
What is Java?
```

---

## Step 3 - Production Log Analysis

Reads production log files.

Example:

```csv
timestamp,model,input_tokens,output_tokens,user
2026-06-01,openrouter/free,1200,400,john
2026-06-01,openrouter/free,2000,800,sarah
```

Extracts:

* Total Requests
* Total Input Tokens
* Total Output Tokens
* Total Tokens Consumed

---

## Step 4 - Carbon Footprint Estimation

Formula:

```text
CO2e = Total Tokens × Emission Factor
```

Current Formula:

```python
carbon = total_tokens * 0.0000005
```

Future versions can integrate:

* ElectricityMap API
* Azure Sustainability APIs
* AWS Customer Carbon Footprint Tool

---

## Step 5 - Intelligent Summary

Generates:

### Executive Summary

Example:

```text
Total Requests: 2
Total Tokens: 4400
Estimated CO2e: 0.0022 kg
```

### Optimization Recommendations

Example:

```text
Reduce prompt length
Cache repeated responses
Use smaller models
Move workloads to low-carbon regions
```

---

# Project Architecture

```text
User
 │
 ▼
Domain Guard Agent
 │
 ▼
Log Parser Agent
 │
 ▼
Carbon Estimator Agent
 │
 ▼
Summary Agent
 │
 ▼
Recommendation Agent
 │
 ▼
Final Report
```

---

# Folder Structure

```text
green_prompt_complete/
│
├── app.py
├── requirements.txt
├── .env.example
│
├── agents/
│   ├── domain_guard.py
│   ├── log_parser.py
│   ├── carbon_estimator.py
│   ├── summary_agent.py
│   └── recommendation_agent.py
│
├── data/
│   └── sample_logs.csv
│
└── README.md
```

---

# API Key Configuration

Create a file named:

```text
.env
```

Add:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Example:

```env
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxx
```

---

# Installation

## Step 1 - Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```bash
python -m venv venv
source venv/bin/activate
```

---

## Step 2 - Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run:

```bash
python app.py
```

Expected Output:

```text
Ask a sustainability question:
```

Example:

```text
Ask a sustainability question:
Estimate carbon footprint
```

Output:

```text
=== SUMMARY ===

Requests: 2
Input Tokens: 3200
Output Tokens: 1200
Estimated CO2e: 0.0022 kg

=== RECOMMENDATIONS ===

1. Reduce prompt length
2. Cache repeated responses
3. Use smaller models
4. Schedule workloads in low-carbon regions
```

---

# Future Roadmap

## Phase 1

* Domain Expert Chatbot
* Log Analysis
* Carbon Calculation

## Phase 2

* OpenRouter LLM Integration
* Intelligent Sustainability Reports

## Phase 3

* RAG (FAISS + Sustainability Policies)
* Carbon Knowledge Base

## Phase 4

* LangGraph Multi-Agent Workflow
* Supervisor Agent
* Tool Calling

## Phase 5

* Streamlit Dashboard
* Real-Time Monitoring
* Enterprise Deployment

---

# Technologies Used

* Python
* OpenRouter
* OpenAI SDK
* Pandas
* LangGraph
* LangChain
* FAISS
* Sentence Transformers
* Streamlit

---

# Business Value

* Supports Net-Zero Initiatives
* Tracks AI Carbon Emissions
* Improves Sustainability Reporting
* Optimizes AI Usage Costs
* Enables Enterprise-Wide AI Governance
