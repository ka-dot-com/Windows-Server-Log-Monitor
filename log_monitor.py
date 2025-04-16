import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def analyze_logs(file_path):
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path, delimiter=";")
        elif file_path.endswith(".json"):
            df = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format. Please use CSV or JSON.")
        
        ip_counts = df.groupby("ip").size().reset_index(name="attempts")
        risky_ips = ip_counts[ip_counts["attempts"] > 5]["ip"].tolist()
        
        return f"Suspicious IPs: {', '.join(risky_ips)}" if risky_ips else "No suspicious activity detected."
    except Exception as e:
        return f"Error: {e}"

def show_gui():
    def load_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            result = analyze_logs(file_path)
            messagebox.showinfo("Analysis Result", result)

    root = tk.Tk()
    root.title("Windows Server Log Monitor")

    tk.Label(root, text="Log Monitor").pack(pady=10)
    tk.Button(root, text="Load Log File", command=load_file).pack(pady=5)
    root.mainloop()

if __name__ == "__main__":
    show_gui()
