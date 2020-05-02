from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

TOP_LINKS = (By.CSS_SELECTOR, "div.Hdr_MN")


@given('Main Page MyRF')
def open_website(context):
    context.driver.get('https://www.raymourflanigan.com/')


@then('User can go through top links and verify page has opened')
def click_thru_top(context):
    WebDriverWait(context.driver, 10).until(
        ec.visibility_of_all_elements_located((By.XPATH, "//a[@ng-if='category.URL'][text()='Kids']")))
    top_links = context.driver.find_elements_by_xpath("//a[@class='Hdr_MNCatLink ng-binding ng-scope']")
    for x in range(0, len(top_links)):
        WebDriverWait(context.driver, 10).until(
            ec.visibility_of_all_elements_located((By.XPATH, "//a[@ng-if='category.URL'][text()='Kids']")))
        top_links = context.driver.find_elements_by_xpath("//a[@class='Hdr_MNCatLink ng-binding ng-scope']")
        top_links[x].click()

