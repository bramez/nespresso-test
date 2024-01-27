from behave import *
from hamcrest import assert_that, is_

from tests.feature.steps.pageobjects.home_page import HomePage
from tests.feature.steps.pageobjects.top_bar_page import TopBar


use_step_matcher("re")


@given("I am on the home page")
def step_impl(context):
    context.home_page = HomePage(context.driver, context.wait)
    context.home_page.accept_cookie_banner()


@step("I click on the login button in the top bar")
def step_impl(context):
    context.top_bar_page = context.top_bar_page.click_login_button()


@step("I enter valid credentials")
def step_impl(context):
    email = "oliaero@gmail.com"
    password = "Chashka2018"

    context.top_bar_page.write_username(email)
    context.top_bar_page.write_password(password)

@when("I click on the login button in the login form")
def step_impl(context):
    context.top_bar_page.click_submit()

@then("I am signed in")
def step_impl(context):
    pass

@step("my name appears in the top bar")
def step_impl(context):
    name = "Olga Erokhina"
    message = context.home_page.get_top_bar_wellcome_message()

    assert_that(name.lower() in message.lower(), is_(True))