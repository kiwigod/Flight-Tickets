from parsers.parserinterface import ParserInterface
from datetime import datetime


class ObjParser(ParserInterface):
    skip = [str, int]

    @staticmethod
    def parse(data):
        # NoneType needs to be specified explicitly..
        if data is None:
            return data

        # skip data types which need no parsing
        if type(data) in ObjParser.skip:
            return str(data)

        if isinstance(data, list):
            return str(len(data))
        elif isinstance(data, datetime):
            return data.__str__()
        return data.__dict__
