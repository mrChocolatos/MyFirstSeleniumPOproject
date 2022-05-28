import os
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
import allure


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose --language: choose any language that do you want")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose --browser_name: choose chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language_name = request.config.getoption("language")
    driver = None
    if browser_name == 'chrome':
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--headless')
        options.add_experimental_option('prefs', {'intl.accept_languages': f'{language_name}'})
        driver = webdriver.Chrome(options=options, executable_path='/app/chromedriver')
    elif browser_name == 'firefox':
        options = webdriver.FirefoxProfile()
        options.set_preference("intl.accept_languages", f'{language_name}')
        driver = webdriver.Firefox(options=options)
    else:
        print('Please, select chrome or firefox bowser')
    yield driver
    print("\nquit browser..")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


#docker run -v /Users/19439211/PycharmProjects/Dockertest/allure-results:/app/allure-results test2 pytest test_product_page.py -s -n 3 --alluredir=allure-results
#docker run -v ${PWD}/allure-results:/app/allure-results -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS:1 frankescobar/allure-docker-service
