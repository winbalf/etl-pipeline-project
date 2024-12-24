import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv
import logging

load_dotenv()  # Load environment variables from .env file

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def load_data(df, db_url):
    try:
        logging.info("Loading data into the database")
        engine = create_engine(db_url)
        with engine.connect() as connection:
            df.to_sql('weather_data', con=connection,
                      if_exists='append', index=False)
        logging.info("Data loading successful")
    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
    except Exception as e:
        logging.error(f"An error occurred during loading: {e}")


if __name__ == "__main__":
    sample_data = {
        "city": "Adelaide",
        "temperature": 20.0,
        "humidity": 78,
        "timestamp": "2024-12-01 00:00"
    }
    df = pd.DataFrame([sample_data])
    db_url = os.getenv("DATABASE_URL")
    load_data(df, db_url)
