from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from time import sleep


class Chrome:
    def __init__(self, driver_file: str, args: list = None, timeout: int = 10):
        self.options = Options()
        self.append_arguments(args)
        self.driver = webdriver.Chrome(driver_file, options=self.options)
        self.driver.set_page_load_timeout(timeout)

    def append_arguments(self, args: list):
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        if args:
            for arg in args:
                self.options.add_argument(arg)

    def get_page(self, url: str):
        self.driver.get(url)

    def enter_text(self, x_path: str, text: str):
        text_field = self.driver.find_element_by_xpath(x_path)
        text_field.send_keys(text)

    def press_button(self, x_path: str):
        button = self.driver.find_element_by_xpath(x_path)
        button.click()

    def get_text(self, x_path: str, retry_attempts: int = 5, retry_delay: int = 1) -> str:
        result = ''
        for _ in range(retry_attempts):
            try:
                result = self.driver.find_element_by_xpath(x_path).text
                break
            except:
                sleep(retry_delay)
        return result

    def get_element_url(self, x_path):
        element = self.driver.find_element_by_xpath(x_path)
        url = element.get_attribute('href')
        return url

    def get_current_url(self) -> str:
        return self.driver.current_url

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()
        self.driver.quit()
