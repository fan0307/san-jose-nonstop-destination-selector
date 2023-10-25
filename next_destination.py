import requests
from bs4 import BeautifulSoup
import random

# Send a GET request to the webpage
url = "https://www.flysanjose.com/nonstop-destinations"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the destinations container
    destinations_container = soup.find("div", class_="views-view-grid horizontal cols-8 clearfix mt-3")

    if destinations_container:
        # Find all card elements within the destinations container
        destinations_list = destinations_container.find_all("div", class_="card")

        if destinations_list:
            # Get the text of each destination and store it in a list
            destinations = [destination.find("h5", class_="card-title h5-responsive").get_text() for destination in destinations_list]

            # Randomly select a destination
            random_destination = random.choice(destinations)

            print(f"Your randomly selected destination is: {random_destination}")
        else:
            print("No destinations found on the page.")
    else:
        print("Destinations container not found on the page.")
else:
    print(f"Failed to retrieve the webpage (status code {response.status_code}).")
