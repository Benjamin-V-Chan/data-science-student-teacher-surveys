import pandas as pd

def summarize_results():
    """Summarize analysis results into a structured report."""
    summary = "Results Summary\n"

    with open("outputs/model_results.txt", "r") as f:
        model_results = f.read()
        summary += "\nModel Results:\n" + model_results

    df_summary = pd.read_csv("outputs/summary_statistics.csv")
    summary += "\nSummary Statistics:\n" + str(df_summary.head())

    with open("outputs/final_report.txt", "w") as f:
        f.write(summary)

if __name__ == "__main__":
    summarize_results()
