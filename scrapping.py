import cloudscraper
import csv
import boto3
import pandas as pd
scraper = cloudscraper.create_scraper()
page = scraper.get('https://finviz.com/screener.ashx?v=410&s=ta_topgainers').text
res = pd.read_html(page)
lst = res[8][0][0].split()
s3 = boto3.client('s3')
bucket_name = 'scraperrresults'
file_name = 'results.csv'
fn = "GFG.csv"
with open(fn,'w') as f:
  csvw =csv.writer(f)
  csvw.writerow(lst)
s3.upload_file(file_name, bucket_name, file_name)
