import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# === Config ===
URL = "https://testautomationpractice.blogspot.com/"


# === Setup driver ===
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

try:
    # Upload single file
    FILE_PATH = r"C:\\Users\\Muskaan\\OneDrive\\Desktop\\SeleniumScripts\\Automation_practice\\resources\\Demo_Document.doc"  
    driver.find_element(By.ID, "singleFileInput").send_keys(FILE_PATH)

    # Submit form
    driver.find_element(By.XPATH, '//*[@id="singleFileForm"]/button').click()

    print("File uploaded successfully.")

    # Upload multiple files
    files = r"C:\\Users\\Muskaan\\Downloads\\demo files\\dummy-pdf_2.pdf" + "\n" + r"C:\\Users\\Muskaan\\Downloads\\demo files\\Demo_Document.pdf"

    # Upload multiple files
    driver.find_element(By.ID, "multipleFilesInput").send_keys(files)

    # Submit form
    driver.find_element(By.XPATH, '//*[@id="multipleFilesForm"]/button').click()

    print("Multiple files uploaded successfully.")


except Exception as e:
    print("Test Failed:", e)

finally:
    time.sleep(5)
    driver.quit()
    
