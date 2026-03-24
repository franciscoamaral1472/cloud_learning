from collections import defaultdict

def detect_bruteforce(logs, threshold=3):
    failed_attempts = defaultdict(int)

    for log in logs:
        if log["action"] == "login_failed":
            failed_attempts[log["ip"]] += 1

    results = []

    for ip, count in failed_attempts.items():
        if count >= threshold:
            results.append({
                "ip": ip,
                "failed_attempts": count,
                "risk": "HIGH"
            })
        elif count > 0:
            results.append({
                "ip": ip,
                "failed_attempts": count,
                "risk": "MEDIUM"
            })

    return results