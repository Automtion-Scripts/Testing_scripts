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

def Select(driver, by, value):
    raise NotImplementedError


def fill_form():
    # Enter Full name
    # full_name = wait.until(EC.presence_of_element_located((By.ID,"name")))
    # full_name.send_keys("Muskaan Sahu")

    # # Enter email
    # email = wait.until(EC.presence_of_element_located((By.ID,"email")))
    # email.send_keys("muskaan@gmail.com")

    # # Phone number
    # phone_number = wait.until(EC.presence_of_element_located((By.ID,"phone")))
    # phone_number.send_keys("9876543210")

    # # Enter current address
    # current_address = wait.until(EC.presence_of_element_located((By.ID,"textarea")))
    # current_address.send_keys("Lit va semblar un simplificat Angles, quam un skeptic Cambridge amico dit me que Occidental es.")

    # Gender radio button
#     Radio_button = ["male","female"] # this logic is also applicable for checkboxes but as the checkbox only select the one option so it select by default last one option
#     for gender in Radio_button:
#         button= wait.until(EC.element_to_be_clickable((By.ID, gender)))
#         button.click()

# #select the day
# days_to_select = ["sunday", "monday", "thursday", "saturday", "wednesday", "friday"] 
# ##"""" if you want to select multiple days so you can use list and loop through it by using for loop""""##

# for day_id in days_to_select:
#     day_element = wait.until(EC.element_to_be_clickable((By.ID, day_id)))
#     day_element.click()

# select the country
    # country_dropdown = wait.until(EC.element_to_be_clickable((By.ID,"country")))
    # country_dropdown.click()
    # option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='country']/option[10]")))
    # option.click()  
    # if option.text == "India":
    #     print("Country selected successfully.")
    

    # country_dropdown = wait.until(EC.element_to_be_clickable((By.ID,"country")))
    # country_dropdown.click()
    # option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='country']/option[1]")))
    # option.click() 

# check scroll bar
    # scroll_bar = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='colors']")))
    # scroll_bar.click()
    # select_color = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='colors']/option[6]")))
    # select_color.click()
    # if select_color.text == "White":
    #     print("Color selected successfully.")
    # else:
    #     print("Color selection failed.")
    # print("Scroll bar clicked successfully.")   
    
# date picker
    # date_picker = wait.until(EC.presence_of_element_located((By.ID,"txtDate")))
    # date_picker.click()
    # date_picker = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"ui-datepicker-month")))
    # date_picker.click()
    # month = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ui-datepicker-div']/div/div/select[1]/option[3]")))
    # month.click()
    # year_picker = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"ui-datepicker-year")))
    # year_picker.click()
    # year = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ui-datepicker-div']/div/div/select[2]/option[3]")))
    # year.click()
    # select_date = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr[5]/td[1]/a")))
    # select_date.click()

    # if date_picker.get_attribute("value") == "26/03/2017":
    #     print("Date selected successfully.")
    # else:
    #     print("Date selection failed.")

#Date range picker
    start_date = wait.until(EC.presence_of_element_located((By.ID, "start-date")))
    start_date.send_keys("10/10/2023")

    end_date = wait.until(EC.presence_of_element_located((By.ID, "end-date")))
    end_date.send_keys("20/10/2023")

    submit_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"submit-btn")))
    submit_button.click()
    print("Date range selected successfully.")
try:
    fill_form()
except Exception as e:
    print("Test Failed:", e)    
finally:
    time.sleep(3)
    driver.quit()
                    
