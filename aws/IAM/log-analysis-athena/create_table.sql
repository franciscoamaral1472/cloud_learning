CREATE EXTERNAL TABLE phishing_logs (
  user string,
  action string,
  ip string,
  timestamp string
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://your-bucket-name/logs/';