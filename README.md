# Stock Sentiment Learning

This repository is a structured learning project focused on building practical skills in Python, Git, and data workflows using stock market data as the working example.

The goal is not to build a production system, but to understand how real-world projects are organized, developed, and iterated on in a clean and reproducible way.

---

## Project Goals

This project is designed to help practice and understand:

- Git and GitHub fundamentals
- Repository structure and organization
- Python scripting
- Virtual environments
- Dependency management
- Fetching and storing external data
- Preparing for future sentiment analysis work

Each step builds incrementally on the previous one.

---

## Repository Structure

```
stock-sentiment-learning/
├── scripts/
│   ├── fetch_stock_data.py
│   ├── analyze_prices.py
│
├── data/
│   ├── .gitkeep
│   └── aapl_prices.csv
│
├── .venv/
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Folder and File Responsibilities

### scripts/
Contains Python scripts that perform a single, clear task.
Scripts should be focused, readable, and runnable from the repository root.

### data/
Stores generated data files such as CSVs.
Data files are created by scripts and not edited manually.

### .venv/
Project-specific virtual environment.
This directory is excluded from Git using `.gitignore`.

### requirements.txt
Lists Python dependencies required to run the project.
Used to recreate the environment consistently.

---

## Setup Instructions

### Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run scripts

```bash
python3 scripts/fetch_stock_data.py
python3 scripts/analyze_prices.py
```

---

## Git and Workflow Best Practices

- One virtual environment per project
- Commit small, logical changes
- Keep generated data separate from scripts
- Use clear commit messages
- Update documentation as the project evolves

---

## Learning Focus

This repository emphasizes:
- Clarity over cleverness
- Structure over speed
- Understanding over automation

Future steps may include:
- Sentiment analysis
- API rate-limit handling
- Logging and error handling
- Data visualization

---

## Status

This is an active learning repository.
Structure and contents may evolve over time.
