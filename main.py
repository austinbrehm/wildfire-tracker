import requests
import typer

URL = "https://eonet.gsfc.nasa.gov/api/v3/events"


def main(state: str, year: str):
    # Get data from NASA EONET API
    request = requests.get(URL)
    data = request.json()

    # Search for wildfire events
    wildfires = []
    events = data["events"]
    for event in events:
        if event["categories"][0]["title"] == "Wildfires":
            title = event["title"]
            if state.lower() in title.lower():
                date = event["geometry"][0]["date"]
                if date.startswith(year):
                    wildfires.append((title, date))

    # Print results
    for title, date in wildfires:
        print(f"🔥 Wildfire Event: {title}, {date}")


if __name__ == "__main__":
    typer.run(main)
