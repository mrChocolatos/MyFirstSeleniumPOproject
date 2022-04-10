from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver


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
        options.add_experimental_option('prefs', {'intl.accept_languages': f'{language_name}'})
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxProfile()
        options.set_preference("intl.accept_languages", f'{language_name}')
        driver = webdriver.Firefox(options=options)
    else:
        print('Please, select chrome or firefox bouwser')
    yield driver
    print("\nquit browser..")
    driver.quit()
