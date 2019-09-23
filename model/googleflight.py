from model.transfer import Transfer
from datetime import datetime


class GoogleFlight:
    def __init__(self, start_dt, end_dt, start_iata, end_iata, airline, duration, price, transfers):
        self.start_dt: datetime = start_dt
        self.end_dt: datetime = end_dt
        self.start_iata: str = start_iata
        self.end_iata: str = end_iata
        self.airline: str = airline
        self.duration: int = duration  # duration in minutes
        self.price: int = price
        self.transfers: [Transfer] = transfers
