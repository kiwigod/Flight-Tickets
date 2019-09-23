from selenium.webdriver.remote.webdriver import WebDriver
from parsers.webparserinterface import WebParserInterface


class Flights(WebParserInterface):
    @staticmethod
    def parse(driver: WebDriver):
        flights = []
        for x in driver.find_elements_by_class_name('gws-flights-results__collapsed-itinerary'):
            flights += [x.text]
        return flights
