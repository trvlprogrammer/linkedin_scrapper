from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time
from apps.utils.config_routes import Linkedin

# function go get cookies from linked using selenium
def linkedin_get_cookies(username=None, password=None):
    try :
        options = webdriver.FirefoxOptions()
        options.headless = True
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(options=options, firefox_profile=fp, executable_path=GeckoDriverManager().install())
        url = Linkedin.base_url + Linkedin.login
        browser.get(url)
        #fill in username and password form and then click login button
        browser.find_element(By.XPATH,"/html/body/div/main/div[2]/div[1]/form/div[1]/input").send_keys(username)
        browser.find_element(By.XPATH,"/html/body/div/main/div[2]/div[1]/form/div[2]/input").send_keys(password)
        browser.find_element(By.XPATH,"/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
        # time.sleep(2)
        cookies = browser.get_cookies()
        li_at = cookies[5]["value"]
        JSESSIONID = cookies[6]["value"]  
        browser.close()  
        return {
            "li_at" : li_at,
            "JSESSIONID" : JSESSIONID
        }
    except Exception as e:
        print(e)




