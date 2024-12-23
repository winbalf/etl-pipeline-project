from flask import Flask, jsonify
from flask_cors import CORS
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)  # Enable CORS


@app.route('/api/weather', methods=['GET'])
def get_weather_data():
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    with engine.connect() as connection:
        df = pd.read_sql('SELECT * FROM weather_data', connection)
    return jsonify(df.to_dict(orient='records'))


def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set")

    print(f"Using API_KEY: {api_key}")  # Add this line to verify

    api_url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q=Adelaide&dt=2024-12-01&end_dt=2024-12-05"
    db_url = "postgresql://postgres:password@db:5432/etl_db"

    raw_data = extract_data(api_url)
    transformed_data = transform_data(raw_data)
    load_data(transformed_data, db_url)


if __name__ == "__main__":
    main()
    app.run(host='0.0.0.0', port=5000)
