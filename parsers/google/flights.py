from parsers.parserinterface import ParserInterface


class Flights(ParserInterface):
    @staticmethod
    def parse(driver):
        flights = []
        for x in driver.find_elements_by_class_name('gws-flights-results__collapsed-itinerary'):
            flights += [x.text]
        return flights
