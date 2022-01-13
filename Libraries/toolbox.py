from Libraries.common import Common
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class ToolBox:
    def __init__(self, toolbox_username, toolbox_password):
        self._web_driver_path = 'C:/Users/aldo.madrid/Documents/AutomationExample/Utilities/Webdrivers/chromedriver.exe'
        self._implicit_wait_time = 10
        self._explicit_wait_time = 30
        self._username = toolbox_username
        self._password = toolbox_password
        self._url_okta = 'https://vzc.okta.com/login/login.htm?fromURI=/app/UserHome'
        self._url_toolbox = 'https://toolbox.telogis.com/otr/index.php'
        try:
            self._start_web_driver()
            self._login_to_okta()
            self._open_toolbox()
        except (NoSuchElementException, TimeoutException):
            print('ToolBox could not be opened, accept Verify notification from okta.')

    def _start_web_driver(self) -> None:
        """Starts Chrome web driver, maximizes window and sets implicit time."""
        print('Starting webdriver.')
        self._driver = Chrome(executable_path=self._web_driver_path)
        self._driver.maximize_window()
        self._driver.implicitly_wait(self._implicit_wait_time)

    def set_implicit_wait_time(self, wait_time) -> None:
        self._driver.implicitly_wait(wait_time)

    def set_explicit_wait_time(self, wait_time) -> None:
        self._explicit_wait_time = wait_time

    def _explicit_wait(self, by, element) -> None:
        """Waits for "explicit_wait_time for element given to be displayed. """
        WebDriverWait(self._driver, self._explicit_wait_time).until(EC.presence_of_element_located((by, element)))

    def _login_to_okta(self) -> None:
        print('Opening okta for username: ' + self._username)
        self._driver.get(self._url_okta)
        self._driver.find_element(By.ID, 'okta-signin-username').send_keys(self._username)
        self._driver.find_element(By.ID, 'okta-signin-submit').click()
        self._explicit_wait(By.XPATH, '//input[@type="password"]')
        self._driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(self._password)
        self._driver.find_element(By.XPATH, '//input[@value="Verify"]').click()
        self._explicit_wait(By.XPATH, '//input[@value="Send Push"]')
        self._driver.find_element(By.XPATH, '//input[@value="Send Push"]').click()

    def _open_toolbox(self) -> None:
        self._explicit_wait(By.XPATH, '//img[@alt="Toolbox logo"]')
        self._driver.find_element(By.XPATH, '//img[@alt="Toolbox logo"]').click()
        tab = self._driver.window_handles
        self._driver.switch_to.window(tab[1])

    def search_new_esn(self, esn: str) -> None:
        try:
            self._driver.get(self._url_toolbox)
            self._driver.find_element(By.ID, 'searchterm').send_keys('vcore 10:0' + esn)
            self._driver.find_element(By.ID, 'gobutton').click()
            if not self._is_esn_found_in_toolbox():
                raise NoSuchElementException
        except (NoSuchElementException, TimeoutException):
            print('No results found for given ESN')

    def _is_esn_found_in_toolbox(self) -> bool:
        is_found_str = self._driver.find_element(By.XPATH, '//td[@align="left"]//h2').text
        return is_found_str.find('returned no results') == -1

    def get_values_in_history_window(self, partial_element_name: str, max_diag_elements_in_page: int = 15) -> list:
        """Once History window is open it captures all values in 'Value' column and return them in a list."""
        if not self._open_diagnostics_element_if_exist(partial_element_name, max_diag_elements_in_page):
            return ['', ]

        try:
            odo_history = self._driver.find_element(
                            By.XPATH, '//table[@class="history"]//tbody//tr//td//span[@class="val"]')
            odo_history = [float(i.text) if Common.is_number(i.text) else i.text for i in odo_history]
            self._driver.find_element(By.ID, 'fancybox-close').click()
        except (NoSuchElementException, TimeoutException):
            odo_history = ['', ]
        return odo_history

    def _open_diagnostics_element_if_exist(self, partial_element_name: str, max_diag_elements_in_page: int = 15) -> bool:
        """Opens given element in the Diagnostics section, 'max_diag_elements_in_page' is number
            of elements to wait to load before start search."""
        try:
            self._explicit_wait(By.XPATH, '//div[contains(@title,"Status:")][' + str(max_diag_elements_in_page) + ']')
            element_index = 0
            for i, element in enumerate(self._driver.find_element(By.CLASS_NAME, 'gps_header')):
                if element.text.find(partial_element_name) != -1:
                    element_index = i + 1
                    break
            self._driver.find_element(By.XPATH, '//div[contains(@title,"Status:")][' + str(element_index) +
                                     ']//div//p//a').click()
            return True
        except (NoSuchElementException, TimeoutException):
            return False





