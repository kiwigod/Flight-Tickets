from selenium.webdriver.remote.webdriver import WebDriver


class WebParserInterface:
    @staticmethod
    def parse(driver: WebDriver):
        raise NotImplementedError()
