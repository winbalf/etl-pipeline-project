import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


def load_data(df, db_url):
    try:
        engine = create_engine(db_url)
        with engine.connect() as connection:
            df.to_sql('weather_data', con=connection,
                      if_exists='append', index=False)
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred during loading: {e}")


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
