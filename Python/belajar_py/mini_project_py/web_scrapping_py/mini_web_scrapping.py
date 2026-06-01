# Date (22/2/26) - (23/2/26)

import csv
import requests
from bs4 import BeautifulSoup



with open("scrap_tim_hoki.csv", "w", newline="", encoding="utf-8") as csvfile:
  fieldnames = ["Team Name", "Year", "Wins", "Losses"]
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()

  for pages in range(1, 25):
    response = requests.get(f'https://www.scrapethissite.com/pages/forms/?page_num={pages}')
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='table')
    team_rows = table.find_all("tr")

    for row in team_rows:
        team_name = row.find("td", class_="name")
        try:
          team_name_data = team_name.text.strip()
        except:
          team_name_data = ""

        year = row.find("td", class_="year")
        try:
          year_data = year.text.strip()
        except:
          year_data= ""

        wins = row.find("td", class_="wins")
        try:
          wins_data = wins.text.strip()
        except:
          wins_data = ""

        losses = row.find("td", class_="losses")
        try:
          losses_data = losses.text.strip()
        except:
          losses_data = ""

        writer.writerow({
          "Team Name": team_name_data,
          "Year": year_data,
          "Wins": wins_data,
          "Losses": losses_data
        })