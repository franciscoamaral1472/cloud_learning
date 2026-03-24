import json
from collections import defaultdict

with open("sample_logs.json") as f:
    logs = json.load(f)

failed_attempts = defaultdict(int)

for log in logs:
    if log["action"] == "login_failed":
        failed_attempts[log["ip"]] += 1

print("Failed login attempts by IP:")
for ip, count in failed_attempts.items():
    print(f"{ip}: {count}")

print("\nSuspicious IPs (>=3 failed attempts):")
for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"{ip} -> potential brute-force attack")