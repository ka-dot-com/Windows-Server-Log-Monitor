# Windows Server Log Monitor

A Python tool to check Windows Server logs for suspicious activity, like too many failed logins. Uses a simple ML model to find outliers and logs alerts.

## How It Works
- Reads CSV logs (e.g., from Event Viewer).
- Counts login attempts per IP.
- Flags unusual activity as potential attacks.
- Writes alerts to `alerts.txt`.

## Setup
1. Install Python 3.8+.
2. Run `pip install -r requirements.txt`.
3. Copy logs to `/logs` (sample file included).
4. Run `python log_monitor.py`.

## Use Case
Helps admins monitor servers without digging through logs. Good for small businesses that need basic security checks.

## Future Improvements
- Add a GUI for non-tech users.
- Support JSON log formats.

Contact: kswierczynska21@gmail.com