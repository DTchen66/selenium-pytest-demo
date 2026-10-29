from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_the_internet_login():
    # service = ChromeService(executable_path="path_to_chromedriver.exe")
    service = ChromeService()  # 使用默认的chromedriver路径

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # 无头模式，不弹浏览器窗口

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    assert "You logged into a secure area!" in driver.page_source
    driver.quit()