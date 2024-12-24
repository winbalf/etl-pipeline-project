import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def transform_data(raw_data):
    try:
        logging.info("Transforming data")
        processed_data = []
        for day in raw_data['forecast']['forecastday']:
            for hour in day['hour']:
                processed_data.append({
                    "city": raw_data["location"]["name"],
                    "temperature": hour["temp_c"],
                    "humidity": hour["humidity"],
                    "timestamp": hour["time"]
                })
        logging.info("Data transformation successful")
        return pd.DataFrame(processed_data)
    except KeyError as e:
        logging.error(f"Key error: {e}")
    except Exception as e:
        logging.error(f"An error occurred during transformation: {e}")


if __name__ == "__main__":
    sample_data = {
        "location": {"name": "Adelaide"},
        "forecast": {
            "forecastday": [
                {
                    "hour": [
                        {"time": "2024-12-01 00:00", "temp_c": 20.0, "humidity": 78},
                        {"time": "2024-12-01 01:00", "temp_c": 19.0, "humidity": 80}
                    ]
                }
            ]
        }
    }
    df = transform_data(sample_data)
    if df is not None:
        print(df)
