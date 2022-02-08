from selenium import webdriver

driver =webdriver.Crome()
driver.get("http://python.org")
driver.save_screenshot("screenshot.png")
driver.quit()
