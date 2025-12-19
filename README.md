# Stock Sentiment Learning Project

This repository is a hands-on learning project designed to build practical skills in:
- Git and GitHub workflows
- Python scripting
- Virtual environments
- Data fetching and analysis
- Foundations for stock sentiment analysis

The project progresses incrementally, with each script serving a clear purpose in a simple data pipeline.

---

## Repository Structure

stock-sentiment-learning/
├── scripts/
│ ├── fetch_prices.py
│ ├── analyze_prices.py
├── data/
│ └── aapl_prices.csv
├── .gitignore
├── README.md

yaml
Copy code

### Folder Overview

- **scripts/**  
  Python scripts for fetching and analyzing data.  
  Scripts are separated by responsibility to keep the workflow clear.

- **data/**  
  Generated data files (CSV).  
  These files are created by scripts and are not edited manually.

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd stock-sentiment-learning
2. Create and activate a virtual environment
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
bash
Copy code
pip install requests
Scripts
fetch_prices.py
Fetches historical stock price data and saves it to a CSV file in the data/ directory.

Example usage:

bash
Copy code
python3 scripts/fetch_prices.py
analyze_prices.py
Reads the CSV file and prints a basic summary of the dataset, including:

Total number of rows

First and last dates

First and last closing prices

Example usage:

bash
Copy code
python3 scripts/analyze_prices.py
Git Workflow
Development is done locally in feature or experiment branches

Changes are committed with clear messages

Code is pushed only when working and reviewed

Data files may be excluded from version control depending on size or source

Learning Goals
This project emphasizes:

Clean separation of concerns

Reproducible environments

Incremental development

Understanding how real-world data pipelines work

Future steps may include:

Text data

Sentiment analysis

API rate limits

Error handling

More advanced data processing

Notes
Python version: 3.x

Tested on macOS

This is a learning repository, not production code