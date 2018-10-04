from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def waituntil(driver, kinds, path = ""):
    wait = WebDriverWait(driver, 10)

    if kinds == 'xpath':
        return wait.until(EC.element_to_be_clickable((By.XPATH, path)))
    elif kinds == 'name':
        return wait.until(EC.element_to_be_clickable((By.NAME, path)))
    elif kinds == 'id':
        return wait.until(EC.element_to_be_clickable((By.ID, path)))
    elif kinds == 'alert':
        wait.until(EC.alert_is_present(),'Timed out waiting for PA creation ' + 'confirmation popup to appear.')

# driver.find_element_by_xpath("//button[@ng-reflect-placeholder='/signup']").click()
