import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

#get row and column count of the table

table = driver.find_element(By.ID, "HTML1")

# Count rows (excluding header row)
rows = table.find_elements(By.XPATH, ".//tr")
print("Row count (including header):", len(rows))

# Count columns (using header row)
cols = table.find_elements(By.XPATH, ".//tr[1]/th")
print("Column count:", len(cols))

driver.quit()