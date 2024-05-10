from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# Created class by name IMDB_Search
class IMDB_Search:
    def __init__(self, driver):
        self.driver = driver

    # Method to start browser and get specified url
    def start(self, url):
        self.url = url
        self.driver.maximize_window()
        self.driver.get(url)

    # Method to scroll window by specified pixels
    def scroll_window_down(self, pixels):
        script = f"window.scrollBy(0, {pixels});"
        self.driver.execute_script(script)

    # Method to pause code execution for specified seconds
    def static_pause(self, seconds):
        start_time = time.time()
        while (time.time() - start_time) < seconds:
            pass

    # Method to search name in filter
    def name_filter(self, name):
        name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-6addea7c-0 dWrCpn'][text()='Name']")))
        name_input.click()

        name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='name-text-input']")))
        name_field.send_keys(name)
        print("Searched for name: Nolan")

    # Method to search for birthdate
    def birth_date(self, dob):
        birth = self.driver.find_element(By.XPATH, "//div[@class='sc-6addea7c-0 dWrCpn'][text()='Birth date']")
        birth.click()

        date = self.driver.find_element(By.XPATH, "//input[@name='birth-date-start-input']")
        date.send_keys(dob)
        print("Birth Date: 30 July 1970")

    # Method to select Awards and Recognition
    def awards_recognition(self):
        awards_select_elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='sc-6addea7c-0 dWrCpn'][text()='Awards & recognition']")))
        awards_select_elem.click()

        oscar = self.driver.find_element(By.XPATH, "//*[@id='accordion-item-awardsAccordion']/div/section/button[10]")
        oscar.click()
        print("Awards and Recognition: Best Director Oscar-Winning")

    # Method to search results
    def see_result(self):
        result = self.driver.find_element(By.XPATH, "//span[@class='ipc-btn__text'][text()='See results']")
        result.click()
        print("Search Successful for Christopher Nolan")

