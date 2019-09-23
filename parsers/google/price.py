from parsers.parserinterface import ParserInterface
import re


class Price(ParserInterface):
    @staticmethod
    def parse(data: str):
        r_price = r'€\s(\d{1,})'
        return re.search(r_price, data).group(1)
