import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 15)

def check_image(image_element):
    if image_element.get_attribute("naturalWidth") == "0":
        print("Image is broken.")
    else:
        print("Image is displayed correctly.")

try:    
    # Wait for the images to load
    images = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
    
    for img in images:
        check_image(img)        

except Exception as e:
    print("Test Failed:", e)    
finally:
    time.sleep(3)
    driver.quit()
