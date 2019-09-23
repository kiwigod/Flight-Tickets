from parsers.parserinterface import ParserInterface
import re


class Time(ParserInterface):
    @staticmethod
    def parse(data: str):
        r_time = r'((\d{2}):(\d{2}))'
        times = re.findall(r_time, data)
        return [int(x) for x in times[0][1:]], [int(x) for x in times[1][1:]]
