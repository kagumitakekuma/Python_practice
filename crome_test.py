from selenium import webdriber
import time

driver =webdriver.Crome()
driver.get("http://python.org")
time.sleep(30)
driver.quit()
