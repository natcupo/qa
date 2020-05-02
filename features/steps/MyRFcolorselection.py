from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By

COLOR_OPTIONS = (By.CSS_SELECTOR, "div.SwatchesContainer")
SELECTED_COLOR = (By.ID, 'ctl00_ctl00_MainContent_uxProduct_uxProductInformation_rpSwatches_ctl04_imgSmallSwatch')


@given('Open Raymour Sofa Page')
def sofa_page_opens(context):
    context.driver.get('https://www.raymourflanigan.com/rockport-microfiber-queen-sleeper-sofa-264298502')


@then('Verify user can select through colors of sofas')
def coloring_loop(context):
    expected_colors = ['Chocolate', 'Conversation Ivory', 'Conversation navy', 'Braxton Charcoal', 'Conversation Capri']
    color_elements = context.driver.find_elements(*COLOR_OPTIONS)
    for x in range(len(color_elements)):
        color_elements[x].click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text

        print('The actual color is: ', actual_color, '.')
        assert actual_color == expected_colors[x], f'Expected {expected_colors[x]}, but got {actual_color} '
