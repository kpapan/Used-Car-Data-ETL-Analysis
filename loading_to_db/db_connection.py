import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

# Load .env file
load_dotenv()

def get_db_url():
    """Constructs the database URL from environment variables."""
    try:
        db_url = (
            f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
            f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        )
        return db_url
    except Exception as e:
        logger.error("Failed to construct DB URL: %s", e)
        raise

def create_db_engine():
    """Creates and returns a SQLAlchemy engine."""
    try:
        db_url = get_db_url()
        engine = create_engine(db_url)
        logger.info("Database engine created successfully.")
        return engine
    except SQLAlchemyError as e:
        logger.error("Database connection error: %s", e)
        raise

def test_connection(engine):
    """Tests the connection to the database."""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()
            logger.info("Connected to DB successfully. Version: %s", version[0])
            return version[0]
    except SQLAlchemyError as e:
        logger.error("Failed to connect to DB: %s", e)
        raise
