from selenium import webdriver
from parsers.google.flights import Flights
from parsers.google.airline import Airline
from parsers.google.duration import Duration
from parsers.google.price import Price
from parsers.google.route import Route
from parsers.google.time import Time
from parsers.google.transfer import Transfer
from model.googleflight import GoogleFlight
from model.url import URL
from datetime import datetime
import re


class Google:
    def __init__(self, driver=webdriver.Firefox()):
        self.driver = driver

    def get(self, url: URL):
        print(type(self).__name__, "- retrieving url:", url.url)
        self.driver.get(url.url)

    def parse(self) -> [GoogleFlight]:
        """
        Parse the retrieved web page
        :return: [GoogleFlight] list of flights proposed by Google
        """
        flights = Flights.parse(self.driver)
        dates = re.findall(r'((\d{4})-(\d{2})-(\d{2}))', self.driver.current_url)
        start_date = [int(x) for x in dates[0][1:]]
        # end_date = [int(x) for x in dates[1][1:]]
        parsed = []
        for flight in flights:
            start_time, end_time = Time.parse(flight)
            start_dt = datetime(start_date[0], start_date[1], start_date[2], start_time[0], start_time[1])
            end_dt = datetime(start_date[0], start_date[1], start_date[2], end_time[0], end_time[1])
            start_iata, end_iata = Route.parse(flight)
            g = GoogleFlight(start_dt, end_dt, start_iata, end_iata, Airline.parse(flight),
                             Duration.parse(flight), Price.parse(flight), Transfer.parse(flight))
            parsed += [g]
        return parsed

    def quit(self):
        self.driver.quit()
