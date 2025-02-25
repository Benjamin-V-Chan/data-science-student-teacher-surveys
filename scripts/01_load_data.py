import pandas as pd

def load_data(file_path):
    """Load dataset from given path and handle missing values."""
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)  # Remove missing values if necessary
    return df

if __name__ == "__main__":
    data_path = 'data/student_feedback.csv'
    output_path = 'outputs/preprocessed_data.csv'
    df = load_data(data_path)
    df.to_csv(output_path, index=False)
