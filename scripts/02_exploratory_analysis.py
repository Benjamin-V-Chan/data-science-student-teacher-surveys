import pandas as pd

def exploratory_analysis(data_path):
    """Perform exploratory data analysis on the dataset."""
    df = pd.read_csv(data_path)
    print(df.info())
    print(df.describe())
    print(df.isnull().sum())

    # Save summary statistics
    df.describe().to_csv("outputs/summary_statistics.csv")

if __name__ == "__main__":
    exploratory_analysis('outputs/preprocessed_data.csv')
