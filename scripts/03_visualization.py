import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_visualizations(data_path):
    """Generate and save visualizations."""
    df = pd.read_csv(data_path)

    # Histogram
    df.hist(figsize=(10, 6))
    plt.savefig("outputs/histograms.png")

    # Correlation heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.savefig("outputs/correlation_heatmap.png")

if __name__ == "__main__":
    generate_visualizations('outputs/preprocessed_data.csv')
