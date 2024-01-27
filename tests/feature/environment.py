from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def before_all(context):
    PATH ="/Users/olia/work/webdrivers/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Iniciar la ventana del navegador maximizada

    context.driver = webdriver.Chrome(PATH, options=options)

    context.wait = WebDriverWait(context.driver, 5)


def after_all(context):
    context.driver.quit()
