import csv
import mechanize
from BeautifulSoup import BeautifulSoup
from tqdm import tqdm
print "Contacting Server..."
print "Fetching details and dumping ..."
list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
for item in tqdm(list):
	for i in tqdm(range(1000,9999)):
		url = 'https://aptransport.in/APCFSTONLINE/Reports/VehicleRegistrationSearch.aspx'
		br = mechanize.Browser()
		resp = br.open(url)
		br.select_form(nr=0)
		br.form['ctl00$OnlineContent$ddlInput'] = ['R']
		br.form['ctl00$OnlineContent$txtInput']='AP31DC'+ str(i)
		response = br.submit()
		html = response.read()
		soup = BeautifulSoup(html)
		table = soup.find('div', attrs={'id': 'ctl00_OnlineContent_tblData'})
		writerr = str(table)
		htmlfile = open("results.html","a")
		htmlfile.write(writerr)
		htmlfile.close()
