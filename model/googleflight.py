from model.transfer import Transfer
from model.db import DB
from datetime import datetime


class GoogleFlight(DB):
    cols = [
        'start_dt',
        'end_dt',
        'start_iata',
        'end_iata',
        'airline',
        'duration',
        'price',
        'transfers',
        'ts'
    ]

    def __init__(self, start_dt, end_dt, start_iata, end_iata, airline, duration, price, transfers):
        super().__init__('tickets', GoogleFlight.cols)
        self.start_dt: datetime = start_dt
        self.end_dt: datetime = end_dt
        self.start_iata: str = start_iata
        self.end_iata: str = end_iata
        self.airline: str = airline
        self.duration: int = duration  # duration in minutes
        self.price: int = price
        self.transfers: [Transfer] = transfers
        self.ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
