from parsers.parserinterface import ParserInterface
from model.transfer import Transfer as T
import re


class Transfer(ParserInterface):
    @staticmethod
    def parse(data: str):
        r_n_transfers = r'(\d)\stussenstop'
        r_transfer = r'(\d{1,})\su (\d{1,})\sm ([A-Z]+)'

        if len(re.findall(r_n_transfers, data)) > 0:
            ts = []
            for transfer in re.findall(r_transfer, data):
                ts += [T(transfer[2], int(transfer[0])*60 + int(transfer[1]))]
            return ts

        return None
