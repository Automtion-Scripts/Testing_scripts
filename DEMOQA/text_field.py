import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 15)

# def basic_validation():
#     """Function to perform basic validation of text fields on the demo page."""
#     #Enter full name
#     full_name = wait.until(EC.presence_of_element_located((By.ID,"userName")))
#     full_name.send_keys("Muskaan Sahu")

#     #Enter email
#     email = wait.until(EC.presence_of_element_located((By.ID,"userEmail")))
#     email.send_keys("muskaan@magureinc.com")

#     #Enter current address
#     current_address = wait.until(EC.presence_of_element_located((By.ID,"currentAddress")))
#     current_address.send_keys("1234 Elm Street, Springfield")

#     #Enter permanent address
#     permanent_address = wait.until(EC.presence_of_element_located((By.ID,"permanentAddress")))
#     permanent_address.send_keys("1234 Elm Street, Springfield")

#     #Click submit
#     Submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#submit")))
#     Submit_button.click()

#     # Validate submission
#     details = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='output']/div")))
#     print("Details:",details.text)
#     print("Basic validation completed successfully.")

# def clear_fields():
#     """Function to clear all text fields."""
#     # Clear full name
#     full_name = wait.until(EC.presence_of_element_located((By.ID,"userName")))
#     full_name.clear()

#     # Clear email
#     email = wait.until(EC.presence_of_element_located((By.ID,"userEmail")))
#     email.clear()

#     # Clear current address
#     current_address = wait.until(EC.presence_of_element_located((By.ID,"currentAddress")))
#     current_address.clear()

#     # Clear permanent address
#     permanent_address = wait.until(EC.presence_of_element_located((By.ID,"permanentAddress")))
#     permanent_address.clear()

#     print ("All fields are cleared successfully.")


# def empty_fields():
#     """Function to test empty fields validation."""
#     # Click submit without entering any data
#     Submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#submit")))
#     Submit_button.click()

#     # Validate that no details are displayed
#     try:
#         details = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='output']/div")))
#         print("Details:", details.text)
#         print("No details displayed as expected.")
#     except Exception as e:
        # print("No details displayed as expected:", e)  

def invalid_email():
    """Function to perform invalid email logic."""
    #Enter full name
    full_name = wait.until(EC.presence_of_element_located((By.ID,"userName")))
    full_name.send_keys("Muskaan Sahu")

    #Enter email
    email = wait.until(EC.presence_of_element_located((By.ID,"userEmail")))
    email.send_keys("muskaan@magureinc")

    #Enter current address
    current_address = wait.until(EC.presence_of_element_located((By.ID,"currentAddress")))
    current_address.send_keys("1234 Elm Street, Springfield")

    #Enter permanent address
    permanent_address = wait.until(EC.presence_of_element_located((By.ID,"permanentAddress")))
    permanent_address.send_keys("1234 Elm Street, Springfield")

def click_submit():
    submit = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit)
    driver.execute_script("arguments[0].click();", submit)

    # validate that the email is invalid
    error_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='userEmail']")))
    error_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='userEmail']")))


try:
    # basic_validation()
    # clear_fields()
    # empty_fields()
    invalid_email()
    click_submit()
    # print("All basic validations completed successfully.")
except Exception as e:
    print("An error occurred during basic validation:", e)
finally:
    time.sleep(5)
    driver.quit()