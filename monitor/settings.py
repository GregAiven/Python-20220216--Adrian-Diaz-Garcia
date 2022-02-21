import os

# Configure here urls and patterns to search on the webs
WEBS = [
    {"url": "https://www.google.es/", "pattern": r"search"},
    {"url": "https://www.google.es/", "pattern": r"look"},
    {"url": "https://www.google.es/", "pattern": r"wat"},
    {"url": "https://www.amazon.es/", "pattern": r"Prime"},
    {"url": "https://www.amazon.es/", "pattern": r"Adrian"},
]


LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER", "kafka:9093")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "web_checks")
