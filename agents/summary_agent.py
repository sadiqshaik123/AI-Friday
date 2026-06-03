
def generate_summary(metrics, carbon):
    return f'''
Requests: {metrics["requests"]}
Input Tokens: {metrics["input_tokens"]}
Output Tokens: {metrics["output_tokens"]}
Estimated CO2e: {carbon:.6f} kg
'''
