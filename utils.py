def validate_log_format(file_path):
    # Check if log file has the right columns
    try:
        df = pd.read_csv(file_path, delimiter=";", nrows=1)
        return all(col in df.columns for col in ["timestamp", "user", "ip", "event"])
    except:
        return False