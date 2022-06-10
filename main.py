from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")

input1 = browser.find_element(By.NAME, 'first_name')
input1.send_keys("Igor")
input2 = browser.find_element(By.NAME, 'last_name')
input2.send_keys("Molchanov")
input3 = browser.find_element(By.CLASS_NAME, 'city')
input3.send_keys("Stavropol")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")

button = browser.find_element(By.TAG_NAME, 'button')
button.click()
