# 第四次运行记录（2026-10-29）

## 用例
test_baidu.py::test_baidu_search

## 现象
使用 Selenium 无头模式打开百度，成功定位到搜索框并输入“pytest selenium”搜索，等待结果页加载时超时两分钟多。

## 报错
test_baidu.py::test_baidu_search - selenium.common.exceptions.TimeoutException: Message:
(Session info: chrome=155.0.8059.86)

## 初步判断
不使用无头模式显示查看浏览器运行发现输入“pytest selenium”搜索后，出现验证拦截页面。
百度风控检测到,网站在拦自动化工具.

## 下一步
别跟百度较劲，换一个练手站点,直接换成专门给自动化测试用的干净站点。