from parsers.parserinterface import ParserInterface
import re


class Duration(ParserInterface):
    @staticmethod
    def parse(data: str):
        r_duration = r'(\d{1,})\su (\d{1,})\sm\n'
        duration = re.findall(r_duration, data)
        duration = [int(x) for x in duration[0]]
        duration[0] *= 60
        duration = sum(duration)
        return duration
