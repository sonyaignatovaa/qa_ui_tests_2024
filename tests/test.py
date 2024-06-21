from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://ya.ru/')
input_search = driver.find_element(By.ID, 'text')
input_search.send_keys('Hello world')
button_search = driver.find_element(By.XPATH, '/html/body/main/div[2]/form/div[3]/button')
button_search.click()
driver.quit()
