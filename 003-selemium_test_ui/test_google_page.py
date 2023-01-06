from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_google_logo_image():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    google_image_element = '/html/body/div[1]/div[2]/div/img'
    google_image = driver.find_element(By.XPATH, google_image_element).is_displayed()
    assert google_image is True


def test_three_icon_in_search_field():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    magnifier_icon_element = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]/div/span"
    mic_icon_element = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[2]"
    camera_icon_element = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[3]/img"
    magnifier_icon = driver.find_element(By.XPATH, magnifier_icon_element).is_displayed()
    mic_icon = driver.find_element(By.XPATH, mic_icon_element).is_displayed()
    camera_icon = driver.find_element(By.XPATH, camera_icon_element).is_displayed()
    assert magnifier_icon is True and mic_icon is True and camera_icon is True


def test_two_button_under_search_field():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    google_search_btn_element = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]"
    lucky_btn_element = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]"
    google_search_btn = driver.find_element(By.XPATH, google_search_btn_element).get_attribute('aria-label')
    assert google_search_btn == "Google 搜尋"
    lucky_btn = driver.find_element(By.XPATH, lucky_btn_element).get_attribute('aria-label')
    assert lucky_btn == "好手氣"


def test_google_btn_upper_left_corner():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    about_google_element = "/html/body/div[1]/div[1]/a[1]"
    google_store_element = "/html/body/div[1]/div[1]/a[2]"
    google_search = driver.find_element(By.XPATH, about_google_element).text
    assert google_search == "關於 Google"
    google_store = driver.find_element(By.XPATH, google_store_element).text
    assert google_store == "Google 商店"
