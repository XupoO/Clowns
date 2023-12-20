from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = 'https://web.telegram.org/k/#@n1njaja'
driver = webdriver.Chrome()
action = ActionChains(driver) 
driver.implicitly_wait(2000000)
driver.get(url=url)
i = -1
lastEll = driver.find_elements(By.CLASS_NAME, "bubble-content-wrapper")[-1]
while True:
    time.sleep(0.3)
    lastEl = driver.find_elements(By.CLASS_NAME, "bubble-content-wrapper")[-1]
    if lastEl==lastEll:

        button = driver.find_elements(By.CLASS_NAME, "bubble-content-wrapper")
        button = button[i]
        i=i-1
        ActionChains(driver)\
            .move_to_element(button)\
            .perform()
        time.sleep(0.3)
        clown = driver.find_element(By.CLASS_NAME, "bubble-hover-reaction")
        clown.click()
        lastEll = driver.find_elements(By.CLASS_NAME, "bubble-content-wrapper")[-1]
    else:
        aboba = driver.find_elements(By.CLASS_NAME, "bubble-content-wrapper")[-1]
        ActionChains(driver)\
            .move_to_element(aboba)\
            .perform()
        aboba.click()
            