from typing import List
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BrowserController:
    def __init__(self, browser_type: str = 'firefox', maximize=False) -> None:
        self.browser_type = browser_type.lower()
        self.maximize = maximize
        self.driver = self._initialize_driver()

    def _initialize_driver(self) -> WebDriver:
        if self.browser_type == 'chrome':
            driver = webdriver.Chrome()
        elif self.browser_type == 'firefox':
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")
        if self.maximize:
            driver.maximize_window()
        return driver

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def close_browser(self) -> None:
        self.driver.quit()

    def get_current_window_handle(self) -> str:
        return self.driver.current_window_handle

    def get_all_window_handles(self) -> List[str]:
        return self.driver.window_handles

    def switch_to_window(self, window_handle: str) -> None:
        self.driver.switch_to.window(window_handle)

    def close_current_window(self) -> None:
        self.driver.close()

    def end(self) -> None:
        self.driver.close()
