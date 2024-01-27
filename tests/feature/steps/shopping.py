from behave import *
from hamcrest import assert_that, is_
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import hamcrest

use_step_matcher("re")


@given("I am on the shopping Coffee page")
def step_impl(context):
    context.driver.get("")
    context.wait.until(EC.visibility_of_element_located((By.)))


@when("I add 10 Napoli capsules")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I add 10 Napoli capsules')


@then("the product is in shopping cart")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the product is in shopping cart')