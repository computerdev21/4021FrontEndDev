import urllib.request
import urllib.parse
import urllib.error
import json
import sys

def search_events(api_key, keyword):
    """
    Searches for events on Ticketmaster using the Discovery API.

    Args:
        api_key (str): Your Ticketmaster API Key.
        keyword (str): The keyword to search for (e.g., artist, event name).
    """
    base_url = "https://app.ticketmaster.com/discovery/v2/events.json"

    # URL encode the parameters
    params = urllib.parse.urlencode({
        "apikey": api_key,
        "keyword": keyword,
        "size": 5  # Limit results to 5
    })

    url = f"{base_url}?{params}"

    print(f"Searching for '{keyword}'...")

    try:
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                print(f"Error: API returned status code {response.status}")
                return

            data = json.loads(response.read().decode())

            # Check if any events were found
            if "_embedded" in data and "events" in data["_embedded"]:
                events = data["_embedded"]["events"]
                print(f"\nFound {len(events)} events:\n")

                for event in events:
                    name = event.get("name", "Unknown Event")
                    dates = event.get("dates", {}).get("start", {}).get("localDate", "Unknown Date")

                    venues = event.get("_embedded", {}).get("venues", [])
                    venue_name = venues[0].get("name", "Unknown Venue") if venues else "Unknown Venue"

                    url = event.get("url", "No URL available")

                    print(f"Event: {name}")
                    print(f"Date:  {dates}")
                    print(f"Venue: {venue_name}")
                    print(f"Link:  {url}")
                    print("-" * 40)
            else:
                print(f"No events found matching '{keyword}'.")

    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        if e.code == 401:
            print("Please check your API Key.")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("--- Ticketmaster Event Search Tool ---")

    # Prompt for API Key
    api_key = input("Enter your Ticketmaster API Key: ").strip()
    if not api_key:
        print("Error: API Key is required.")
        return

    # Prompt for search keyword
    keyword = input("Enter a keyword to search for (e.g., 'Taylor Swift', 'New York'): ").strip()
    if not keyword:
        print("Error: Search keyword is required.")
        return

    search_events(api_key, keyword)

if __name__ == "__main__":
    main()
