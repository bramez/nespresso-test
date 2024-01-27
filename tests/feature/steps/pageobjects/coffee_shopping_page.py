from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


class CoffeeShoppingPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        self.wait_until_loaded()

    def wait_until_loaded(self):
        # follow redirects are not currently working, so I'm forcing to load the page
        self.driver.get("https://www.nespresso.com/es/en/order/capsules/original")
        # voy a poner las condiciones que hacen qeu mi login page esté completamente cargado
        self.wait.until(EC.visibility_of_element_located((By.ID, 'plp-filter-cta')))

    def get_page_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".h-3xl-700").text

    def find_original_coffees_title(self):
        self.driver.find_element(By.ID, 'plp-filter-cta')

    def click_napoli_add_to_basket(self):
        napoli_add_button = self.driver.find_element(By.ID, 'AddToBagButton__button-CremaComponentId-19')
        napoli_add_button.click()

    def select_capsules_quatity(self):
        quantity_button = self.driver.find_element(By.ID, 'ta - quantity - selector__predefined - 1')
        quantity_button.click()
