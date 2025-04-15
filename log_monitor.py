import pandas as pd
import os
from sklearn.ensemble import IsolationForest
from datetime import datetime

def analyze_logs(log_file):
    # Load logs, expecting CSV from Windows Event Viewer
    try:
        df = pd.read_csv(log_file, delimiter=";", usecols=["timestamp", "user", "ip", "event"])
    except FileNotFoundError:
        print(f"Error: {log_file} not found. Check /logs folder.")
        return
    
    # Count login attempts per IP to spot unusual patterns
    ip_counts = df.groupby("ip").size().reset_index(name="attempts")
    model = IsolationForest(contamination=0.05, random_state=42)
    
    # Look for outliers that might be attacks
    anomalies = model.fit_predict(ip_counts[["attempts"]])
    risky_ips = ip_counts[anomalies == -1]["ip"].tolist()
    
    # Save alerts if something looks off
    if risky_ips:
        alert = f"{datetime.now()}: Suspicious IPs detected: {risky_ips}"
        print(alert)
        with open("alerts.txt", "a") as f:
            f.write(alert + "\n")
    else:
        print("All clear, no issues.")

if __name__ == "__main__":
    log_path = "logs/security_log.csv"
    print("Starting Windows Server Log Monitor...")
    while True:
        if os.path.exists(log_path):
            analyze_logs(log_path)
        else:
            print("Waiting for log files...")
        # Check every 10 seconds to avoid high CPU usage
        import time
        time.sleep(10)