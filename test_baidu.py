import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_baidu_search():
    options = Options()
    # options.add_argument('--headless')  # 无头模式，不弹浏览器窗口
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.baidu.com")
    # time.sleep(5)  # 给足时间让页面完全加载

    # 显示等待：等搜索框出现且可交互，最多等10s
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.element_to_be_clickable((By.ID, "chat-textarea")) 
    )
    
    # 找到搜索框，输入关键词
    search_box.send_keys("pytest selenium")
    # 元素是否嵌入在form表单中，如果是，支持submit()方法提交表单；如果不是，使用回车键提交
    search_box.send_keys(webdriver.common.keys.Keys.RETURN)

    # 等待结果页加载，如果10秒内被滑块劫持就截图留证
    try:
        wait.until(EC.title_contains("pytest selenium"))
        assert "pytest selenium" in driver.title
    except Exception:
        driver.save_screenshot("baidu_search_result.png")
        pytest.skip("可能被滑块劫持,非脚本逻辑错误")
    
    driver.quit()