-- Count requests per IP
SELECT sourceIPAddress, COUNT(*) as request_count
FROM logs
GROUP BY sourceIPAddress
ORDER BY request_count DESC;

-- Detect suspicious IPs (threshold example)
SELECT sourceIPAddress
FROM logs
GROUP BY sourceIPAddress
HAVING COUNT(*) > 2;

-- Access pattern over time
SELECT eventTime, sourceIPAddress
FROM logs
ORDER BY eventTime;