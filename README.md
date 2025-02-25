# data-science-student-teacher-surveys

# Project Overview
This project analyzes student feedback responses to assess teaching effectiveness. It includes data preprocessing, exploratory analysis, visualization, and modeling to derive insights.

# Folder Structure
```
project-root/
├── data/                    # Store the dataset
│   └── student_feedback.csv  # Input data file
├── scripts/                 # Store analysis scripts
│   ├── 01_load_data.py
│   ├── 02_exploratory_analysis.py
│   ├── 03_visualization.py
│   ├── 04_modeling.py
│   └── 05_results_summary.py
├── outputs/                 # Store generated results
│   ├── preprocessed_data.csv
│   ├── summary_statistics.csv
│   ├── histograms.png
│   ├── correlation_heatmap.png
│   ├── model_results.txt
│   ├── final_report.txt
├── requirements.txt         # Required dependencies
└── README.md                # Project documentation
```

# Usage
### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```sh
pip install -r requirements.txt
```

### 2. Run the Scripts:

#### Load and preprocess the dataset:
```sh
python scripts/01_load_data.py
```

#### Perform exploratory analysis:
```sh
python scripts/02_exploratory_analysis.py
```

#### Generate visualizations:
```sh
python scripts/03_visualization.py
```

#### Train a model on student feedback data:
```sh
python scripts/04_modeling.py
```

#### Summarize analysis results:
```sh
python scripts/05_results_summary.py
```

# Requirements
- Python 3.x
- Required libraries are listed in `requirements.txt`

# Acknowledgments
**Dataset Name:** Student Feedback Survey Responses  
**Dataset Author:** Ruchi Bhatia  
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/ruchi798/student-feedback-survey-responses/data)