import boto3
import cloudscraper
import csv
import pandas

scraper = cloudscraper.create_scraper()
page = scraper.get('https://finviz.com/screener.ashx?v=410&s=ta_top Gainers').text
res = pandas.read_html(page)
lst = res[8][0][0].split()

fn = "results.csv"
with open(fn,'w') as f:
  csvw = csv.writer(f)
  for item in lst:
    csvw.writerow([item])

# Upload the result to S3
s3 = boto3.client('s3')
s3.upload_file(fn, 'scraperrresults', fn)
