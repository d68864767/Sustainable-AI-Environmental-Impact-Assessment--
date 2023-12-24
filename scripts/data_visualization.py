```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File paths for the processed data
cleaned_data_path = '../data/processed/cleaned_data.csv'
transformed_data_path = '../data/processed/transformed_data.csv'

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def visualize_data(df):
    # Create a pairplot to visualize the relationships between variables
    sns.pairplot(df)
    plt.show()

    # Create a heatmap to visualize the correlation between variables
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.show()

def main():
    # Load and visualize cleaned data
    cleaned_data = load_data(cleaned_data_path)
    print("Visualizing cleaned data...")
    visualize_data(cleaned_data)

    # Load and visualize transformed data
    transformed_data = load_data(transformed_data_path)
    print("Visualizing transformed data...")
    visualize_data(transformed_data)

if __name__ == "__main__":
    main()
```
