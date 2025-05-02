import argparse
import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_data(limit=None):
    url = 'https://www.lemonade.com/pet/explained/cost-vet-visit/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    header = [cell.text.strip() for cell in rows[0].find_all(['th', 'td'])][:2]

    data = []
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) >= 2:
            data.append([cols[0].text.strip(), cols[1].text.strip()])
            if limit and len(data) >= limit:
                break

    return header, data

def save_to_csv(header, data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

if __name__ == "__main__":
    header, data = scrape_data()
    save_to_csv(header, data, 'data/raw/Vet_Visit_Cost_Raw.csv')

