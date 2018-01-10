from bs4 import BeautifulSoup
#from selenium import webdriver
import requests
import shutil

dev_url = "https://rent.591.com.tw/rent-detail-5928170.html"

head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
res = requests.get(dev_url, headers = head)
soup = BeautifulSoup(res.text, 'lxml')


phone_img = soup.find("div", {"class":"infoTwo clearfix"}).find("img")['src'].split('//')[-1]
img = 'https://'+phone_img
prin(img)

imgraw = requests.get(img, stream=True)
f = open('haha.png' , 'wb')
#dev_house.dev_phone_img=shutil.copyfileobj(imgraw.raw, f)
shutil.copyfileobj(imgraw.raw, f)
#shutil.move()
f.close
del imgraw


