from behave import *
from hamcrest import assert_that, is_
from selenium.common import NoSuchElementException

from tests.feature.steps.pageobjects.coffee_shopping_page import CoffeeShoppingPage
from tests.feature.steps.pageobjects.top_bar_page import TopBar
from tests.feature.steps.pageobjects.home_page import HomePage

use_step_matcher("re")


@when("I click the coffee icon in menu bar")
def step_impl(context):
    context.coffee_shopping_page = context.home_page.click_coffee_icon_in_menu_bar()


@then("I can see the shopping Coffee page")
def step_impl(context):
    # This step is just informative, as the page object is loaded before when th click is performed
    pass
    assert_that(context.coffee_shopping_page.get_page_title().lower(), "original coffees")


@given("I am logged in")
def step_impl(context):
    context.home_page = HomePage(context.driver, context.wait)
    context.home_page.accept_cookie_banner()
    context.top_bar_page = context.home_page.click_login_button()

    email = "oliaero@gmail.com"
    password = "Chashka2018"

    context.top_bar_page.write_username(email)
    context.top_bar_page.write_password(password)
    context.top_bar_page.click_submit()


@step("I am on the shopping Coffee page")
def step_impl(context):
    context.coffee_shopping_page = CoffeeShoppingPage(context.driver, context.wait)


@when("I add 10 Napoli capsules")
def step_impl(context):
    context.coffee_shopping_page.click_napoli_add_to_basket()
    # choose the quantity in drop-down menu
    context.coffee_shopping_page.select_capsules_quatity()


@then("the product is in shopping cart")
def step_impl(context):
    context.top_bar_page.click_your_basket_button()

    try:
        go_to_checkout_button = context.top_bar_page.find_go_to_checkout_button()
        assert_that(go_to_checkout_button.is_displayed(), is_(True))
    except NoSuchElementException:
        assert False
