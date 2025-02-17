import requests
import argparse

def get_coordinates(api_key, location):
    """
    Retrieve latitude and longitude for a given city or town using the MapQuest Geocoding API.
    """
    url = "http://www.mapquestapi.com/geocoding/v1/address"
    params = {
        "key": api_key,
        "location": location
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Check for a successful API response (statuscode 0 indicates success)
        if data.get("info", {}).get("statuscode") == 0:
            location_data = data["results"][0]["locations"][0]["latLng"]
            return location_data["lat"], location_data["lng"]
        else:
            print("API error:", data.get("info", {}).get("messages"))
    else:
        print("HTTP error:", response.status_code)
    return None, None

def main():
    parser = argparse.ArgumentParser(
        description="Retrieve latitude and longitude for a given city or town using the MapQuest Geocoding API."
    )
    parser.add_argument("location", help="City or town name")
    parser.add_argument("--api-key", required=True, help="MapQuest API key")
    args = parser.parse_args()

    lat, lng = get_coordinates(args.api_key, args.location)

    if lat is not None and lng is not None:
        print(f"Latitude: {lat}, Longitude: {lng}")
    else:
        print("Could not retrieve the coordinates for the provided location.")

if __name__ == "__main__":
    main()