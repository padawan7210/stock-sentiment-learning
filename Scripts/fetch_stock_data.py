import requests

t ="cvna"

url = "https://stooq.com/q/d/l/?s=" + t + ".us&i=d"

response = requests.get(url)

if response.status_code == 200:
    with open("data/" + t + "_prices.csv", "w") as file:
        file.write(response.text)
    print("Stock data saved successfully")
else:
    print("Failed to fetch data:", response.status_code)
