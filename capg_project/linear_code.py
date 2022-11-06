import time

from selenium import webdriver

path = r"C:\Users\Shankar Kadam\PycharmProjects\capg_project\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://in.bookmyshow.com/")
driver.get(path)
driver.maximize_window()
driver.implicitly_wait(20)

# driver.find_element("xpath", '//input[@type="text"]').send_keys("Bengaluru")
# driver.find_element("xpath", '//strong[text()="Bengaluru"]').click()
driver.find_element("xpath", '//a[text()="Events"]').click()
driver.find_element("xpath", '(//div[text()="Browse by Venues"])[1]').click()
driver.find_element("xpath", '//div[text()="Art Beat: Bengaluru"]').click()
driver.find_element("xpath", '//img[@alt="Texture painting on canvas"]').click()
driver.find_element("xpath", '//button[text()="Book"]').click()
driver.find_element("xpath", '//div[text()="Add"]').click()
driver.find_element("id", 'booking-proceed-button').click()
driver.find_element("xpath", '//input[@name="name"]').send_keys('Shankar')
driver.find_element("xpath", '//input[@type="number"]').send_keys('9359233886')
driver.find_element("xpath", '//input[@type="email"]').send_keys('kadamshankar668@gmail.com')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.find_element("xpath", '//input[@type="checkbox"]').click()
# driver.find_element("id", 'registration-submit-button').click()
# driver.find_element("xpath", '//button[text()="Login to Proceed"]').click()
