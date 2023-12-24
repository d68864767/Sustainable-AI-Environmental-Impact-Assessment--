```python
# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler

# File paths for the raw data
climate_data_path = '../data/raw/climate_data.csv'
air_quality_data_path = '../data/raw/air_quality_data.csv'
biodiversity_data_path = '../data/raw/biodiversity_data.csv'

# File paths for the processed data
cleaned_data_path = '../data/processed/cleaned_data.csv'
transformed_data_path = '../data/processed/transformed_data.csv'

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    df = df.dropna()  # Remove rows with missing values
    df = df.drop_duplicates()  # Remove duplicate rows
    return df

def transform_data(df):
    scaler = StandardScaler()
    df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def main():
    # Load, clean, transform and save climate data
    climate_data = load_data(climate_data_path)
    cleaned_climate_data = clean_data(climate_data)
    transformed_climate_data = transform_data(cleaned_climate_data)
    save_data(transformed_climate_data, cleaned_data_path)

    # Load, clean, transform and save air quality data
    air_quality_data = load_data(air_quality_data_path)
    cleaned_air_quality_data = clean_data(air_quality_data)
    transformed_air_quality_data = transform_data(cleaned_air_quality_data)
    save_data(transformed_air_quality_data, cleaned_data_path)

    # Load, clean, transform and save biodiversity data
    biodiversity_data = load_data(biodiversity_data_path)
    cleaned_biodiversity_data = clean_data(biodiversity_data)
    transformed_biodiversity_data = transform_data(cleaned_biodiversity_data)
    save_data(transformed_biodiversity_data, cleaned_data_path)

if __name__ == "__main__":
    main()
```
