import requests


def extract_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


if __name__ == "__main__":
    api_url = "http://api.weatherapi.com/v1/history.json?key=YOUR_API_KEY&q=Adelaide&dt=2024-12-01&end_dt=2024-12-05"
    data = extract_data(api_url)
    print(data)
