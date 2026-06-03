
EMISSION_FACTOR = 0.0000005

def estimate_carbon(metrics):
    total_tokens = metrics["input_tokens"] + metrics["output_tokens"]
    return total_tokens * EMISSION_FACTOR
