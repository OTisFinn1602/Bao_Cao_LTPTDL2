# from matplotlib.pyplot import text

# import csv
# from csv import reader
# from nbformat import write
import requests
from bs4 import BeautifulSoup

# x = requests.get("https://www.stockbiz.vn/Stocks/STB/HistoricalQuotes.aspx")
# x1 = "VND"
# x2 = "STB"
# x3 = "HPG"
# x4 = "SSI"
# x5 = "GEX"
x = ["VND", "STB", "HPG", "SSI", "GEX"]
i = 0
while i < 5:
    resp = requests.get(
        'https://www.stockbiz.vn/Stocks/' + x[i] + '/HistoricalQuotes.aspx')
    soup = BeautifulSoup(resp.content, 'html.parser')
    links = soup.select_one('.dataTable')
    links = str(links)
    links = links.replace(
        '<table border="0" cellpadding="2" cellspacing="0" class="dataTable" width="100%">', "")
    links = links.replace('</table>', "")
    links = links.replace('\n', "")
    links = links.replace('\r', "")
    links = links.replace('  ', "")
    links = links.replace('<tr>', "")
    links = links.replace('</tr>', "\n")
    links = links.replace('<th>', "")
    links = links.replace('<th align="left">', "")
    links = links.replace('<th align="right">', "")
    #####
    links = links.replace(',', ".")
    links = links.replace('</th>', ",")
    #
    links = links.replace('\xa0,', "")
    links = links.replace('<td>', "")
    links = links.replace('<td align="right">', "")
    ######
    links = links.replace('</td>', ",")
    links = links.replace(',\n', "\n")
    #
    links = links.replace('<tr class="stripe">', "")
    links = links.replace('<span class="quoteup">', "")
    links = links.replace('<span class="quotedown">', "")
    links = links.replace('</span>', "")

    # print(links)
    f = open("Data.csv", "a", encoding="utf-8")
    f.write(str(links))
    f.close
    i += 1


# html = x.text

# start = html.find(
#     '<div id="ctl00_webPartManager_wp1770166562_wp1427611561_callbackData" style="">')

# start = html.find("05/10/2022")
# # end = html.find('<div class="dividerInlineH">&nbsp;</div>')
# end = html.find('<div class="dividerInlineH">')

# html = html[start:end]

# # html = html.replace()
# html = html.replace(
#     '<div id="ctl00_webPartManager_wp1770166562_wp1427611561_callbackData" style="">', "")
# html = html.replace(
#     '<table width="100%" cellspacing="0" cellpadding="2" border="0" class="dataTable">', "")
# html = html.replace('<tr>', "")
# html = html.replace('</tr>', "")
# html = html.replace('<th align="left">', "")
# html = html.replace('<th align="right">', "")
# html = html.replace('<th>', "")
# html = html.replace('</th>', "")
# html = html.replace('&nbsp;', "")

# html = html.replace('<td>', "")
# html = html.replace('</td>', "")
# html = html.replace('<td align="right">', "")
# html = html.replace('<a id="ctl00_webPartManager_wp1770166562_wp1427611561_rptQuotes_ctl01_lnkChart" href="https://www.stockbiz.vn/Stocks/STB/LookupQuote.aspx?Date=14/10/2022"><img src="/ESImages/chart.gif" style="border-width:0px;" /></a>', "")

# print(html)
