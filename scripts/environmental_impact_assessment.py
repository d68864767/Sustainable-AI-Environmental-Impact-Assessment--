```python
# Import necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# File paths for the processed data
cleaned_data_path = '../data/processed/cleaned_data.csv'
transformed_data_path = '../data/processed/transformed_data.csv'

# File paths for the models
gpt4_model_path = '../data/models/gpt4_model/'
machine_learning_model_path = '../data/models/machine_learning_model/'

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def split_data(df):
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

def save_model(model, file_path):
    model.save(file_path)

def main():
    # Load the cleaned and transformed data
    cleaned_data = load_data(cleaned_data_path)
    transformed_data = load_data(transformed_data_path)

    # Split the data into training and testing sets
    X_train_clean, X_test_clean, y_train_clean, y_test_clean = split_data(cleaned_data)
    X_train_transformed, X_test_transformed, y_train_transformed, y_test_transformed = split_data(transformed_data)

    # Train and evaluate the models on the cleaned data
    model_clean = train_model(X_train_clean, y_train_clean)
    evaluate_model(model_clean, X_test_clean, y_test_clean)

    # Train and evaluate the models on the transformed data
    model_transformed = train_model(X_train_transformed, y_train_transformed)
    evaluate_model(model_transformed, X_test_transformed, y_test_transformed)

    # Save the models
    save_model(model_clean, machine_learning_model_path + 'model_clean')
    save_model(model_transformed, machine_learning_model_path + 'model_transformed')

if __name__ == "__main__":
    main()
```
