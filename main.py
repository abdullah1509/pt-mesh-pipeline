import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = "http://en.chinabidding.mofcom.gov.cn/"

# Sending GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    tender_elements = soup.find_all("div", class_="news-item fr")
    print(tender_elements, "data")

    csv_file = "tender_data.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Title", "Published Date", "Deadline", "Link"])

        for element in tender_elements:
            title = element.find("span", class_="txt-02")
            published_date = element.find("span", class_="txt-02")
            deadline = element.find("span", class_="txt-02")
            link = url + element.find("a")["href"]
            csv_writer.writerow([title, published_date, deadline, link])

    print("Scraping and CSV creation successful!")
else:
    print("Failed to retrieve the webpage.")

print("Printing Data:")
sc_data = pd.read_csv('tender_data.csv')
print(sc_data)
