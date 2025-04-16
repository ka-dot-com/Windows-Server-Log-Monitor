import pandas as pd
import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)

def validate_log_format(file_path):
    try:
        df = pd.read_csv(file_path, delimiter=";", nrows=1)
        return all(col in df.columns for col in ["timestamp", "user", "ip", "event"])
    except Exception as e:
        logging.error(f"Error validating log format: {e}")
        return False
