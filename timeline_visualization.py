import matplotlib.pyplot as plt
from datetime import datetime

def visualize_timeline(events):
    dates = [datetime.strptime(event["timestamp"], "%Y-%m-%d %H:%M:%S") for event in events]
    labels = [event["action"] for event in events]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, range(len(dates)), marker="o", linestyle="-", color="blue")
    plt.xticks(rotation=45)
    plt.yticks(range(len(dates)), labels)
    plt.title("Timeline of Activities")
    plt.xlabel("Timestamp")
    plt.ylabel("Action")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    events = [
        {"timestamp": "2025-01-01 10:00:00", "action": "File recovered"},
        {"timestamp": "2025-01-01 12:00:00", "action": "Metadata extracted"},
    ]
    visualize_timeline(events)
