from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

def waituntil(driver, kinds, path = ""):
    if kinds == 'xpath':
        return WebDriverWait(driver, 10) \
            .until(EC.element_to_be_clickable((By.XPATH, path)))
    elif kinds == 'name':
        return WebDriverWait(driver, 10) \
            .until(EC.element_to_be_clickable((By.NAME, path)))
    elif kinds == 'id':
        return WebDriverWait(driver, 10) \
            .until(EC.element_to_be_clickable((By.ID, path)))
    elif kinds == 'alert':
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
            'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
