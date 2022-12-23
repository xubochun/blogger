from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import example_1_element as e1e


service = Service(executable_path="/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Go to stock yahoo! webpage
driver.get('https://tw.stock.yahoo.com/')

# Search stock symbol
driver.find_element(By.XPATH, e1e.SEARCH_BAR).send_keys('2330')

# Click on the enter
ActionChains(driver).send_keys(Keys.ENTER).perform()

# Get the data of the stock
stock_data = driver.find_element(By.XPATH, e1e.STOCK_DATA)

# Get the open, close... price
datas = stock_data.find_elements(By.TAG_NAME, 'li')

target = {
    '成交': '',
    '開盤': '',
    '最高': '',
    '最低': '',
    '均價': ''
}

for i in range(5):
    # print(datas[i].text)
    if list(target)[i] in datas[i].text:
        target[list(target)[i]] = datas[i].text.split()[1]

