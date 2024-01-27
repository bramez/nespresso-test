from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from tests.feature.steps.pageobjects.coffee_shopping_page import CoffeeShoppingPage
from tests.feature.steps.pageobjects.top_bar_page import TopBar


class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        self.wait_until_loaded()

    def wait_until_loaded(self):
        self.driver.get("https://www.nespresso.com/es/en/")
        # voy a poner las condiciones que hacen qeu mi login page esté completamente cargado

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.LoginDropdownButton')))
        self.accept_cookie_banner()

    def click_login_button(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, '.LoginDropdownButton')
        login_button.click()

        return TopBar(self.driver, self.wait)

    def get_top_bar_wellcome_message(self):
        return self.driver.find_element(By.ID, 'ta-login-dropdown--logged').text

    def accept_cookie_banner(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
            accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_button.click()
        except TimeoutException:
            print ("Cookie banner did not appear. Continue")

    def click_coffee_icon_in_menu_bar(self):
        coffee_icon = self.driver.find_element(By.CSS_SELECTOR, '[data-qa=menu_coffee]')
        coffee_icon.click()

        return CoffeeShoppingPage(self.driver, self.wait)
