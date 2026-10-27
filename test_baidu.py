import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_baidu_search():
    options = Options()
    options.add_argument('--headless')  # 无头模式，不弹浏览器窗口
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.baidu.com")
    
    # 找到搜索框，输入关键词
    search_box = driver.find_element(By.ID, "kw")
    search_box.send_keys("pytest selenium")
    search_box.submit()
    
    # 验证搜索结果页标题包含关键词
    assert "pytest selenium" in driver.title
    
    driver.quit()