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
    try:
        db_url = os.getenv("DATABASE_URL")
        engine = create_engine(db_url)
        with engine.connect() as connection:
            df = pd.read_sql('SELECT * FROM weather_data', connection)
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def run_etl():
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable not set")

        api_url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q=Adelaide&dt=2024-12-01&end_dt=2024-12-05"
        db_url = os.getenv("DATABASE_URL")

        raw_data = extract_data(api_url)
        if raw_data:
            transformed_data = transform_data(raw_data)
            if transformed_data is not None:
                load_data(transformed_data, db_url)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_etl()
    app.run(host='0.0.0.0', port=5000)
