import csv

file_path = "data/aapl_prices.csv"

with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print("Total rows:", len(rows))

first_row = rows[0]
last_row = rows[-1]

print("First date:", first_row["Date"])
print("Last date:", last_row["Date"])
print("First close price:", first_row["Close"])
print("Last close price:", last_row["Close"])
