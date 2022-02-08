from selenium import webdriver

driver =webdriver.Chrome()
driver.get("https://www.yahoo.co.jp/")
driver.save_screenshot("screenshot1.png")
driver.quit()
