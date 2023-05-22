import pytest
from selenium import webdriver
from selene import browser, by, be, have

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture(params=[(1920, 1080), (1600, 1200), (2650, 1440)])
def web_browser_for_github_desktop(request):
	chrome_options = webdriver.ChromeOptions()
	browser.config.driver_options = chrome_options
	browser.config.window_height = request.param[0]
	browser.config.window_width = request.param[1]
	yield browser
	browser.quit()


@pytest.fixture(params=[(240, 320), (320, 568), (360, 640)])
def web_browser_for_github_mobile(request):
	chrome_options = webdriver.ChromeOptions()
	browser.config.driver_options = chrome_options
	browser.config.window_height = request.param[0]
	browser.config.window_width = request.param[1]
	yield browser
	browser.quit()


def test_github_desktop(web_browser_for_desktop):
    browser.open('https://github.com/')
    browser.element('a.HeaderMenu-link--sign-in').click()


def test_github_mobile(web_browser_for_mobile):
    browser.open('https://github.com/')
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link[href="/pricing"]').click()
