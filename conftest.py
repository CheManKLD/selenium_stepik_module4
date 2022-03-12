import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en, ru, ... (etc.)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        browser = webdriver.Firefox(firefox_profile=fp, firefox_binary=binary)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
