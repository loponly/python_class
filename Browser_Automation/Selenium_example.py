
# pip install webdriver-manager
# pip install selenium

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()

options.add_argument('download.default_directory=../driver/')

# options.add_argument('--proxy-server=http://192.168.1.1:8080')
# options.add_argument(
#     'user-agent=Mozilla: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101')

#    if kwargs.get("headless"):
#         options.add_argument('--headless')
#     if kwargs.get("no_sandbox"):
#         options.add_argument('--no-sandbox')
#     if kwargs.get("disable_shm"):
#         options.add_argument('--disable-dev-shm-usage')
#     if kwargs.get("disable_notifications"):
#         options.add_argument('--disable-notifications')
#     if kwargs.get("window_size"):
#         options.add_argument(
#             '--window-size={}'.format(kwargs.get("window_size")))
#     if kwargs.get("dev_tools_port"):
#         options.add_argument(
#             '--remote-debugging-port={port}'.format(port=kwargs.get("dev_tools_port")))
#     if kwargs.get("extensions"):
#         for extension in kwargs.get("extensions"):

# options.add_extension('extension.crx')

#     if kwargs.get("user_data_dir"):
# options.add_argument('user-data-dir=user_data_dir')
#     return options

options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
options.add_argument('--download.default_directory=../download')


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Enter your url
driver.get('https://103.229.178.4:444/login')

# Element Selector
username = driver.find_element_by_css_selector('input[name="username"]')
password = driver.find_element_by_css_selector('input[name="secretkey"]')

button = driver.find_element_by_css_selector('button.primary')

username.send_keys('test')
password.send_keys('test')

button.click()

# wait function


def wait_until(driver, selector_text):
    return WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, selector_text)))


def click_element(dirver, menu_name):
    elements = driver.find_elements_by_css_selector(
        'span.ng-binding')

    # element.click()
    # element.send_keys() -> input type
    # element.clear() -> clears input
    # element.text -> returns inner string
    # element.tag_name -> tag name
    # element.get_attribute('href')

    for element in elements:
        if element.text.strip() == menu_name:
            element.click()
            return True
    return False


if wait_until(driver, 'div[ng-click="navbarCtrl.navbar.entryClicked(entry)"]'):
    if click_element(driver, 'Log & Report'):
        if click_element(driver, 'User Events'):
            if wait_until(driver, 'f-icon.fa-download.ng-scope'):
                download = driver.find_element_by_css_selector(
                    'f-icon.fa-download.ng-scope')

                print(download.click())

            # user_event.click()
            # django, flask , torrando
            # Pgui
            # elem.send_keys('iphone')
            # Cython

# driver.quit()
