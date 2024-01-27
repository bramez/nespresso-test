from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.wait_until_loaded()

    def wait_until_loaded(self):
        # voy a poner las condiciones que hacen qeu mi login page esté completamente cargado
        self.wait.until(EC.visibility_of_element_located((By.ID, 'ta-login-form__submit')))

    def write_username(self, username):
        self.driver.find_element(By.ID, "ta-header-username").send_keys(username)

    def write_password(self, password):
        self.driver.find_element(By.ID, "ta-header-password").send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.ID, 'ta-login-form__submit').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'ta-login-dropdown--logged')))



#def accept_cookie_banner():
#    context.wait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
#    accept_button = context.driver.find_element(By.ID, "onetrust-accept-btn-handler")
#    accept_button.click()