from selenium import webdriver  

driver = webdriver.Chrome()  
driver.get("https://example.com/login")  

driver.find_element("id", "username").send_keys("user")  
driver.find_element("id", "password").send_keys("pass123")  
driver.find_element("id", "submit").click()  

assert "Welcome" in driver.page_source  