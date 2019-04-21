import pytest
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


# @pytest.fixture(scope="module")
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_homepage(live_server, driver):
    driver.get(live_server.url)
    expected = "Pur Beurre - Du gras, oui, mais de qualité"
    assert driver.title == expected
