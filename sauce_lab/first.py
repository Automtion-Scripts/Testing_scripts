from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver

options = ChromeOptions()
options.browser_version = 'latest'
options.platform_name = 'Windows 11'
sauce_options = {}
sauce_options['username'] = 'oauth-muskaans1341-b3a1c'
sauce_options['accessKey'] = '532963de-bc92-4f4d-835e-1d8749706ddb'
sauce_options['build'] = 'selenium-build-A757D'
sauce_options['name'] = '<Muskaan Sahu'
options.set_capability('sauce:options', sauce_options)

url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"
driver = webdriver.Remote(command_executor=url, options=options)  
# run commands and assertions
driver.get("https://www.saucedemo.com")
title = driver.title
titleIsCorrect = "Swag Labs" in title
jobStatus = "passed" if titleIsCorrect else "failed"

# end the session
driver.execute_script("sauce:job-result=" + jobStatus)
driver.quit()