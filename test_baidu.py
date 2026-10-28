import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_baidu_search():
    options = Options()
    options.add_argument('--headless')  # 无头模式，不弹浏览器窗口
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.baidu.com")

    # 显示等待：等搜索框出现且可交互，最多等10s
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.element_to_be_clickable((By.ID, "kw"))
    )
    
    # 找到搜索框，输入关键词
    search_box.send_keys("pytest selenium")
    search_box.submit()

    # 等待结果页加载
    wait.until(EC.title_contains("pytest selenium"))    
    # 验证搜索结果页标题包含关键词
    assert "pytest selenium" in driver.title
    
    driver.quit()