# Web Scrapping
import urllib.request
from bs4 import BeautifulSoup
import csv

# URL
# url = 'https://www.nhsinform.scot/illnesses-and-conditions/a-to-z'
# # Fetching the html
# request = urllib.request.Request(url)
# content = urllib.request.urlopen(request)
# # Parsing the html
# parse = BeautifulSoup(content, 'html.parser')
# # Provide html elements' attributes to extract the data
# text1 = parse.find_all('h2', attrs={'class': 'module__title'})
# # text2 = parse.find_all('p', attrs={'class': 'module__desc'})
#
# print(text1)
# # print(" space ")
# # print(text2)
#
# # Writing extracted data in a csv file
# with open('Conditions.csv', 'a', newline="") as csv_file:
#   writer = csv.writer(csv_file)
#   # writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
#   writer.writerow(['Condition'])
#   for col1 in text1:
#     writer.writerow([col1.get_text().strip()])



# # URL
# url = 'https://www.healthywa.wa.gov.au/Health-conditions/Health-conditions-A-to-Z'
# # url = 'https://www.nhsinform.scot/illnesses-and-conditions/a-to-z'
#
# # Fetching the html
# request = urllib.request.Request(url)
# content = urllib.request.urlopen(request)
# # Parsing the html
# parse = BeautifulSoup(content, 'html.parser')
# # Provide html elements' attributes to extract the data
# # text1 = parse.find_all('h2', attrs={'class': 'module__title'})
# # text1 = parse.find_all('div', attrs={'class': 'az-result D-letter'})
# text1 = parse.select('a[id*="phmaincontent_1_rptGroupHeadings_rptArticles_"]')
#
# # text2 = parse.find_all('p', attrs={'class': 'module__desc'})
#
# print(text1)
# # print(" space ")
# # print(text2)
#
# # Writing extracted data in a csv file
# with open('Conditions.csv', 'a', newline="") as csv_file:
#   writer = csv.writer(csv_file)
#   # writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
#   # writer.writerow(['Condition'])
#   for col1 in text1:
#     writer.writerow([col1.get_text().strip()])



from urllib.request import Request, urlopen


# URL
url = 'https://www.hrcsonline.net/health-categories/'

# Fetching the html
# request = urllib.request.Request(url)
# content = urllib.request.urlopen(request)

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urlopen(req).read()

# Parsing the html
parse = BeautifulSoup(content, 'html.parser')
# Provide html elements' attributes to extract the data
text1 = parse.find_all('h3', attrs={'class': 'feature-box__title'})
# text1 = parse.find_all('div', attrs={'class': 'az-result D-letter'})
# text1 = parse.select('a[id*="phmaincontent_1_rptGroupHeadings_rptArticles_"]')

# text2 = parse.find_all('p', attrs={'class': 'module__desc'})

print(text1)
# print(" space ")
# print(text2)

# Writing extracted data in a csv file
with open('Condition_catagories.csv', 'a', newline="") as csv_file:
  writer = csv.writer(csv_file)
  # writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  # writer.writerow(['Condition'])
  for col1 in text1:
    writer.writerow([col1.get_text().strip()])