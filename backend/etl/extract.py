import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


def extract_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set")

    api_url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q=Adelaide&dt=2024-12-01&end_dt=2024-12-05"
    data = extract_data(api_url)
    print(data)
