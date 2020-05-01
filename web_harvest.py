from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("D:\Campus\Pythons\chromedriver.exe")
judul=[] #yang mau di harvest
# url web
driver.get("https://www.cnnindonesia.com/")
content = driver.page_source
soup = BeautifulSoup(content)
for harvest in soup.findAll('article'):
	name=harvest.find('h2', attrs={'class':'title'})
	judul.append(name.text)

	df = pd.DataFrame({'Judul Berita':judul}) 
	df.to_csv('hasil.csv', index=False, encoding='utf-8')
