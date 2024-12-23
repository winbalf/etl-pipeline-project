import pandas as pd


def transform_data(raw_data):
    processed_data = []
    for day in raw_data['forecast']['forecastday']:
        for hour in day['hour']:
            processed_data.append({
                "city": raw_data["location"]["name"],
                "temperature": hour["temp_c"],
                "humidity": hour["humidity"],
                "timestamp": hour["time"]
            })
    return pd.DataFrame(processed_data)


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
    print(df)