```python
# Import necessary libraries
import pandas as pd
import time
from datetime import datetime

# File paths for the processed data
cleaned_data_path = '../data/processed/cleaned_data.csv'
transformed_data_path = '../data/processed/transformed_data.csv'

# File paths for the raw data
climate_data_path = '../data/raw/climate_data.csv'
air_quality_data_path = '../data/raw/air_quality_data.csv'
biodiversity_data_path = '../data/raw/biodiversity_data.csv'

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def monitor_data():
    while True:
        # Load the data
        climate_data = load_data(climate_data_path)
        air_quality_data = load_data(air_quality_data_path)
        biodiversity_data = load_data(biodiversity_data_path)

        # Print the latest data
        print(f"Latest Climate Data: \n{climate_data.tail(1)}")
        print(f"Latest Air Quality Data: \n{air_quality_data.tail(1)}")
        print(f"Latest Biodiversity Data: \n{biodiversity_data.tail(1)}")

        # Wait for a specified amount of time (e.g., 5 seconds) before the next iteration
        time.sleep(5)

def main():
    print("Starting real-time data monitoring...")
    monitor_data()

if __name__ == "__main__":
    main()
```
