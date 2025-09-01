from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Click link that opens new tab (buttons)
# driver.find_element(By.XPATH, "//*[@id='HTML4']/div[1]/button").click()
# time.sleep(2)

# # Get window handles
# handles = driver.window_handles    #returns a list of all tabs/windows currently open.
# print("All window handles:", handles)

# # Switch to new tab (last handle in the list)
# driver.switch_to.window(handles[-1]) #changes focus from the current tab to another tab.
# print("Now on new tab, title:", driver.title)  #gets the page title of the current tab to confirm switch.

# # Do something in new tab
# print(driver.find_element(By.TAG_NAME, "h3").text)

# # Switch back to original tab
# driver.switch_to.window(handles[0])  #Switches back to the first tab (original tab).
# print("Back to original tab, title:", driver.title)   #confirms switch back by printing title.


# check the new tab functionality with link
driver.find_element(By.XPATH, "//*[@id='HTML16']/div[1]/a").click()
time.sleep(2)

# Get window handles
handles = driver.window_handles    #returns a list of all tabs/windows currently open.
print("All window handles:", handles)

# Switch to new tab (last handle in the list)
driver.switch_to.window(handles[-1]) #changes focus from the current tab to another tab.
print("Now on new tab, title:", driver.title)  #gets the page title of the current tab to confirm switch.

# Do something in new tab
print(driver.find_element(By.TAG_NAME, "h3").text)

# Switch back to original tab
driver.switch_to.window(handles[0])  #Switches back to the first tab (original tab).
print("Back to original tab, title:", driver.title) 


driver.quit()
