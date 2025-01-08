from flask import Flask, jsonify
from flask_cors import CORS
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import logging
import requests

# Load environment variables from .env file
load_dotenv()  

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

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
        logging.error(f"An error occurred while fetching weather data: {e}")
        return jsonify({"error": str(e)}), 500


def check_api_status(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            logging.info("API is working")
            return True
        else:
            logging.error(f"API returned status code {response.status_code}")
            return False
    except requests.RequestException as e:
        logging.error(f"An error occurred while checking API status: {e}")
        return False


def validate_data(df):
    if df.isnull().values.any():
        logging.error("Data contains null values")
        return False
    if not all(df.columns == ["city", "temperature", "humidity", "timestamp", "version"]):
        logging.error("Data schema mismatch")
        return False
    return True

def run_etl():
    try:
        api_key = os.getenv("API_KEY")
        api_base_url = os.getenv("API_BASE_URL")
        api_city = os.getenv("API_CITY")
        api_start_date = os.getenv("API_START_DATE")
        api_end_date = os.getenv("API_END_DATE")
        db_url = os.getenv("DATABASE_URL")
        version = 1  # Set the version number

        if not api_key or not api_base_url or not api_city or not api_start_date or not api_end_date:
            raise ValueError("One or more API environment variables are not set")

        api_url = f"{api_base_url}?key={api_key}&q={api_city}&dt={api_start_date}&end_dt={api_end_date}"

        if not check_api_status(api_url):
            raise ValueError("API is not working")

        logging.info("Starting ETL process")
        raw_data = extract_data(api_url)
        if raw_data:
            transformed_data = transform_data(raw_data, version)
            if transformed_data is not None and validate_data(transformed_data):
                load_data(transformed_data, db_url)
        logging.info("ETL process completed successfully")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    run_etl()
    app.run(host='0.0.0.0', port=5000)
