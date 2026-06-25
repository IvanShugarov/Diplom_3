import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-features=PasswordWeaknessCheck,PasswordLeakDetection")
        web_driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
    yield web_driver
    web_driver.quit()

@pytest.fixture()
def user_data():
    payload = {
    "email": "ivanivan@yandex.ru",
    "password": "краска7"
}
    yield payload