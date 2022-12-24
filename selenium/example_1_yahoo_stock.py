from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import example_1_element as e1e


service = Service(executable_path="/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

# Go to stock yahoo! webpage
print('[INFO] Go to Yahoo! Stock website.')
driver.get('https://tw.stock.yahoo.com/')

# Search stock symbol
print('[INFO] Search Stock: 2330')
WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(e1e.SEARCH_BAR))
driver.find_element(*e1e.SEARCH_BAR).send_keys('2330')

# Click on the enter
print('[INFO] send key: enter')
WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(e1e.TSMC))
ActionChains(driver).send_keys(Keys.ENTER).perform()

# Get the data of the stock
WebDriverWait(driver, 10).until(EC.presence_of_element_located(e1e.STOCK_DATA))
stock_data = driver.find_element(*e1e.STOCK_DATA)

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

print(target)
