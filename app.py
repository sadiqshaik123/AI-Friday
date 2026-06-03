
from dotenv import load_dotenv
import os
from agents.domain_guard import is_allowed_question
from agents.log_parser import parse_logs
from agents.carbon_estimator import estimate_carbon
from agents.summary_agent import generate_summary
from agents.recommendation_agent import generate_recommendations

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("OPENROUTER_API_KEY missing in .env")
    exit()

question = input("Ask a sustainability question: ")

if not is_allowed_question(question):
    print("Only sustainability and AI carbon footprint questions are allowed.")
    exit()

metrics = parse_logs("data/sample_logs.csv")
carbon = estimate_carbon(metrics)
summary = generate_summary(metrics, carbon)
recommendations = generate_recommendations(metrics)

print("\n=== SUMMARY ===")
print(summary)

print("\n=== RECOMMENDATIONS ===")
print(recommendations)
