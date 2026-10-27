# 第一次运行记录（2026-10-25）

## 用例
test_baidu.py::test_baidu_search

## 现象
使用 Selenium 无头模式打开百度，定位搜索框后 send_keys 报错。

## 报错
selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
(Session info: chrome=155.0.8059.86)

## 初步判断
元素已找到但不可交互，可能是页面未完全渲染或存在遮挡。

## 下一步
改用 WebDriverWait + element_to_be_clickable 重试。