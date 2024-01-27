from behave import *
from hamcrest import assert_that, is_
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import hamcrest

use_step_matcher("re")


@given("I am on the home page")
def step_impl(context):
    context.driver.get("https://www.nespresso.com/es/en/")

    context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.LoginDropdownButton')))
    print ("Page loaded")


@step("I click on the login button in the top bar")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
    accept_button = context.driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_button.click()

    login_button = context.driver.find_element(By.ID, 'ta-login-dropdown--not-logged')
    login_button.click()
    # login_button = context.driver.find_element(By.CSS_SELECTOR, '.LoginDropdownButton')
    # login_button.click()

    # wait until login form opens
    context.wait.until(EC.visibility_of_element_located((By.ID, 'ta-login-form__submit')))

@step("I enter valid credentials")
def step_impl(context):
    email = "oliaero@gmail.com"
    password = "Chashka2018"

    # write email
    context.driver.find_element(By.ID, "ta-header-username").send_keys(email)

    #write password
    context.driver.find_element(By.ID, "ta-header-password").send_keys(password)



@when("I click on the login button in the login form")
def step_impl(context):
    context.driver.find_element(By.ID, 'ta-login-form__submit').click()


@then("I am signed in")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.ID, 'ta-login-dropdown--logged')))

@step("my name appears in the top bar")
def step_impl(context):
    name = "Olga Erokhina"
    message = context.driver.find_element(By.ID, 'ta-login-dropdown--logged').text

    assert_that(name.lower() in message.lower(), is_(True))