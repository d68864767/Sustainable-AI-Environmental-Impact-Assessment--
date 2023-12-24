```python
# Import necessary libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# URLs for the data sources
climate_data_url = 'your_climate_data_source_url'
air_quality_data_url = 'your_air_quality_data_source_url'
biodiversity_data_url = 'your_biodiversity_data_source_url'

def fetch_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def parse_data(soup):
    data = []
    table = soup.find('table')
    table_rows = table.find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        data.append(row)

    return data

def save_data(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def main():
    # Fetch and save climate data
    climate_data = fetch_data(climate_data_url)
    parsed_climate_data = parse_data(climate_data)
    save_data(parsed_climate_data, '../data/raw/climate_data.csv')

    # Fetch and save air quality data
    air_quality_data = fetch_data(air_quality_data_url)
    parsed_air_quality_data = parse_data(air_quality_data)
    save_data(parsed_air_quality_data, '../data/raw/air_quality_data.csv')

    # Fetch and save biodiversity data
    biodiversity_data = fetch_data(biodiversity_data_url)
    parsed_biodiversity_data = parse_data(biodiversity_data)
    save_data(parsed_biodiversity_data, '../data/raw/biodiversity_data.csv')

if __name__ == "__main__":
    main()
```
