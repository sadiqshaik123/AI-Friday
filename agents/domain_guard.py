
ALLOWED = [
    "carbon",
    "sustainability",
    "emission",
    "co2",
    "llm",
    "green ai"
]

def is_allowed_question(question):
    q = question.lower()
    return any(word in q for word in ALLOWED)
