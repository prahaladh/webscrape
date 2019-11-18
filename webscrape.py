import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all('table')[0] 
    list_of_rows = []
    for row in table.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll(["th","td"]):
             text = cell.text
             list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    print(list_of_rows)


url="https://www.w3schools.com/html/tryit.asp?filename=tryhtml_tables2"
get_data(url)

