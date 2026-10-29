# 第二次运行记录（2026-10-28）

## 用例
test_baidu.py::test_baidu_search

## 现象
使用 Selenium 无头模式打开百度，显示等搜索框出现且可交互，最多等10s，超时报错。

## 报错
selenium.common.exceptions.TimeoutException: Message:
(Session info: chrome=155.0.8059.86)

## 初步判断
元素已找到，加入等待10s后仍不可交互，保留页面未完全渲染或存在遮挡的可能，大概率是百度首页有登录弹窗或者Cookie提示挡住了

## 下一步
改用 WebDriverWait + element_to_be_clickable 重试。

## 最终原因
百度搜索框已经不是kw，kw是一个活化石，它已经被弃用了，chat-textarea才是现在的百度搜索框id。

## 引出问题

### 定位元素
selenium是一个自动化模拟用操作浏览器中的元素的工具，首先应准确确定位到网页中的元素。
方法一：右键检查
方法二：使用开发者工具中的_选择元素_工具
方法三：在控制台中用js验证
举例，document.querySelector('#kw').style.border = '3px solid red' 可以使id为kw的元素被红色框圈住

### pytest临时调试
方案 1：pytest 里加 --pdb（最推荐，零代码改动）
方案 2：在代码里加 input() 暂停（最简单粗暴）
方案 3：失败时自动截图 + 保留浏览器（pytest 风格）