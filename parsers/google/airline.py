from parsers.parserinterface import ParserInterface
import re


class Airline(ParserInterface):
    @staticmethod
    def parse(data: str):
        r_airline = r'^([A-Z][A-Z|a-z]+(,?\s[A-Z][A-Z|a-z]+){0,}?(,?\s[A-Z][A-Z|a-z]+){0,}?)$'
        return re.findall(r_airline, data, re.M)[0][0]
