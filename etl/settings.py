import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER", "kafka:9093")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "web_checks")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "web_checks_group")
KAFKA_BATCH_SIZE = int(os.getenv("KAFKA_BATCH_SIZE", 5))
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_USER = os.getenv("PGUSER", "aivenu")
DB_PASSWORD = os.getenv("PGPASSWORD", "aivenp")
DB_DATABASE = os.getenv("DB_DATABASE", "postgres")
