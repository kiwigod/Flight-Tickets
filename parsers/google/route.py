from parsers.parserinterface import ParserInterface
import re


class Route(ParserInterface):
    @staticmethod
    def parse(data: str):
        r_route = r'([A-Z]{3})–([A-Z]{3})'
        iatas = re.search(r_route, data)
        return iatas[1], iatas[2]
