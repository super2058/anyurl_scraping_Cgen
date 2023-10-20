import time
import json
import hashlib
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from setting import *
from functions import *
import os

DELAY_TIME=1
INFO_SAVE_FOLDER="C:/RAW/"

def click_button(driver, css_selector, delay_time, attempts, success_message, error_message):
    while attempts:
        time.sleep(delay_time)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            button = driver.find_element(By.CSS_SELECTOR, css_selector)
            button.click()
            print(success_message)
        except:
            print(error_message)
            break
        attempts=attempts-1
    if attempts: return False
    return True

    
def get_url_content(driver, my_url):
    driver.get(my_url)
    raw_content = driver.execute_script('return document.querySelector("body").textContent;')
    return raw_content

def save_raw_content(raw_content, url_unique_key):
    data = {"content": raw_content}
    with open(INFO_SAVE_FOLDER + url_unique_key, "w") as file:
        file.write(json.dumps(data))

    
if __name__ == '__main__':
    
    if not os.path.exists(INFO_SAVE_FOLDER):
        os.makedirs(INFO_SAVE_FOLDER)
        print("Folder created successfully!")
    else:
        print("Folder already exists.")
    
    any_url = input("Enter your url:")
    
    driver = webdriver.Chrome()    
    driver.get(any_url)
    click_button(driver, '[class*="ch2-btn ch2-allow-all-btn ch2-btn-primary"]', DELAY_TIME, 1, "Succeed", "Can't Click accept all button!")
     # Click Next Button
    time.sleep(1)
    

    print(any_url)
    md5_hash = hashlib.md5()
    md5_hash.update(any_url.encode())
    url_unique_key = md5_hash.hexdigest()
    raw_content = get_url_content(driver, any_url)
    
    save_raw_content(raw_content, url_unique_key)