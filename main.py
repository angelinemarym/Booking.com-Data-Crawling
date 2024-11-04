import requests
from bs4 import BeautifulSoup
import json

def save_data_to_json(data):
    json_object = json.dumps(data, indent=4)
    with open('booking_hotels_result.json', 'w') as outfile:
        outfile.write(json_object)

def main():
    # Booking.com URL to search hotels in Bali, Indonesia - Feel free to change the URL
    search_page_url = 'https://www.booking.com/searchresults.html?ss=Bali&ssne=Bali&ssne_untouched=Bali&label=gen173nr-1FCAEoggI46AdIM1gEaGiIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Ar68orkGwAIB0gIkYWQ0ZjE0ZDgtNzI5Zi00MjY5LWExMmYtZGNkZTAxMzVkN2U02AIF4AIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=835&dest_type=region&checkin=2024-12-22&checkout=2024-12-25&group_adults=2&no_rooms=1&group_children=0'

    response = requests.get(search_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    hotels_list = []

    hotel_cards = soup.find_all('div', {'data-testid': 'property-card'})

    for idx, hotel in enumerate(hotel_cards):
        hotel_dict = {}

        # Extract hotel name
        title = hotel.find('div', {'data-testid': 'title'})
        hotel_dict['name'] = title.text

        # Extract hotel page URL
        title_link = hotel.find('a', {'data-testid': 'title-link'})
        hotel_dict['page_url'] = title_link['href']

        # Request HTML elements for each hotel page
        hotel_page = requests.get(hotel_dict['page_url'])
        hotel_page_soup = BeautifulSoup(hotel_page.text, 'html.parser')

        # Extract hotel description
        descriptions = hotel_page_soup.find_all('div', class_ = 'hp_desc_main_content')
        temp_descs = ""
        for description in descriptions:
            temp_descs += description.text
        hotel_dict['description'] = temp_descs

        # Extract top 5 hotel images
        images = hotel_page_soup.find_all('img', class_ = 'hide')
        temp_images = []
        for image in images:
            temp_images.append(image['src'])
            if len(temp_images) == 5:
                break
        hotel_dict['images'] = temp_images

        hotels_list.append(hotel_dict)

        print(f"{idx + 1}. Crawled {hotel_dict['name']} hotel")

        # Limit to first 20 hotels
        if len(hotels_list) == 20:
            break

    # Save data to JSON file
    save_data_to_json(hotels_list)
    print('Data crawling process finished. The data is stored in the booking_hotels_result.json file.')

if __name__ == '__main__':
    main()
