
import pandas as pd

def parse_logs(file_path):
    df = pd.read_csv(file_path)

    return {
        "requests": len(df),
        "input_tokens": int(df["input_tokens"].sum()),
        "output_tokens": int(df["output_tokens"].sum())
    }
