import psycopg2
from sqlalchemy import create_engine


def load_data(df, db_url):
    engine = create_engine(db_url)
    with engine.connect() as connection:
        df.to_sql('weather_data', con=connection,
                  if_exists='append', index=False)


if __name__ == "__main__":
    import pandas as pd
    sample_data = {
        "city": "Adelaide",
        "temperature": 20.0,
        "humidity": 78,
        "timestamp": "2024-12-01 00:00"
    }
    df = pd.DataFrame([sample_data])
    db_url = "postgresql://postgres:password@localhost:5432/etl_db"
    load_data(df, db_url)
