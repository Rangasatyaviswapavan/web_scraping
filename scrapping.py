import cloudscraper
import csv
import pandas as pd
scraper = cloudscraper.create_scraper()
page = scraper.get('https://finviz.com/screener.ashx?v=410&s=ta_topgainers').text
res = pd.read_html(page)
lst = res[8][0][0].split()
fn = "GFG.csv"
with open(fn,'w') as f:
  csvw =csv.writer(f)
  csvw.writerow(lst)