from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    executable_path=ChromeDriverManager().install(),
    options=options
)


driver.get('http://unegui.mn')
elem = driver.find_elements_by_css_selector(
    '.js-query-search.js-suggest-input')

elem.send_keys('iphone')
options = driver.find_element_by_css_selector('option')
