import pandas as pd
import csv
import os
import argparse
import wget
from selenium import webdriver
from selenium.webdriver.common.by import By
from driversetup import *

p = argparse.ArgumentParser()
p.add_argument('--url', '-u', type=str)
p.add_argument('--folder', '-f', type=str)
args = p.parse_args()

#use capital on first letter
url = args.url
directory = args.folder

driver = driversetup()
driver.get(url)
lnks=driver.find_elements(By.TAG_NAME, 'audio')
print(len(lnks))
data = []
for lnk in lnks:
    link = lnk.get_attribute('src')
    data.append(link)

driver.close()

os.system('mkdir ' + directory)
os.chdir(directory)

for links in data:
    wget.download(links)
