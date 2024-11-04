# Booking.com Data Crawling Script

This Python script crawls hotel data from the Booking.com website. The `requests` module is used to retrieve the page content, while `BeautifulSoup4` simplifies parsing the webpage information into HTML format.

## Data Structure

The script crawls a maximum of 20 hotels, with each hotel having up to 5 image URLs. General information, including the hotel name, URL, and description, is scraped. The final results are stored in a JSON file. Here is an example of the stored data structure:

```
[
    {
        "name": "North Wing Canggu Resort",
        "page_url": "https://www.booking.com/hotel/id/north-wing-canggu-resort-kabupaten-badung.html?ucfs=1&arphpl=1&dest_id=835&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=00c54d3a2c3d0379&srepoch=1730717942&from_sustainable_property_sr=1&from=searchresults",
        "description": "\n\nYou might be eligible for a Genius discount at North Wing Canggu Resort. Sign in to check if a Genius discount is available for your selected dates.\n\n\nGenius discounts at this property are subject to booking dates, stay dates, and other available deals.\n\nLocated in Dalung, 5.7 miles from Ubung Bus Station, North Wing Canggu Resort has accommodations with an outdoor swimming pool, free private parking, a garden and a shared lounge. Offering a bar, the property is located within 6.3 miles of Petitenget Temple. The property provides a 24-hour front desk, airport transportation, room service and free WiFi.\n\nAt the resort the rooms are equipped with air conditioning, a desk, a terrace with a pool view, a private bathroom, a flat-screen TV, bed linen and towels. All rooms feature a closet.\n\nBreakfast is available every morning, and includes \u00e0 la carte, continental and American options. At North Wing Canggu Resort you'll find a restaurant serving American, Chinese and French cuisine. Dairy-free and halal options can also be requested.\n\nThe area is popular for cycling, and bike rental and car rental are available at the accommodation.\n\nTanah Lot Temple is 7.2 miles from North Wing Canggu Resort, while Bali Museum is 7.9 miles from the property. Ngurah Rai International Airport is 11 miles away.Distance in property description is calculated using \u00a9 OpenStreetMap\n",
        "images": [
            "https://cf.bstatic.com/xdata/images/hotel/max1024x768/509296417.jpg?k=f8a1277ab9259651a6d24cf8dad278c9d954e7bd9af975876789fb6ca6c4ed1d&o=&hp=1",
            "https://cf.bstatic.com/xdata/images/hotel/max500/509283846.jpg?k=344fc61675bb299ccbc7f603d90bbd33db06c8c5bd36441ecdafca4be2fc1968&o=&hp=1",
            "https://cf.bstatic.com/xdata/images/hotel/max500/509294351.jpg?k=8fe366cb5137fc583dd7cc7eedb052e5043990d6c828dbed06021e76ab8e1313&o=&hp=1",
            "https://cf.bstatic.com/xdata/images/hotel/max300/388300867.jpg?k=d6546578873cf91f96bdf4aa4cd21fcbff3e44ac8308cd72bf7d59786423d3b3&o=&hp=1",
            "https://cf.bstatic.com/xdata/images/hotel/max300/518298293.jpg?k=bdac34b5999e2f0a8a842b94f4a8fb045aec15d50e4e3f05544c6863f73f4d90&o=&hp=1"
        ]
    }
]
```

## Installation

Before running the script, follow these installation steps:
- (Optional: create & activate a virtual environment) virtualenv venv, then source venv/bin/activate
- `pip install -r requirements.txt`

## Usage

Run the script with the following command:
```
python3 booking_scraper.py
```

## Additional information

To scrape hotels in a different city, change the webpage URL in the `search_page_url` variable:
```
search_page_url = '{{booking.com hotel search url}}'
```

