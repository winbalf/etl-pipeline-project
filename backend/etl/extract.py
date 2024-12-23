import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


def extract_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set")

    api_url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q=Adelaide&dt=2024-12-01&end_dt=2024-12-05"
    data = extract_data(api_url)
    if data:
        print(data)
