from model.urlparam import URLParam


class URL:
    def __init__(self, url, url_param):
        self.url: str = url
        self.url_param: URLParam = url_param

    def set_route(self, start_iata, end_iata):
        self.url = self.url.replace(self.url_param.start_iata, start_iata)
        self.url = self.url.replace(self.url_param.end_iata, end_iata)

    def set_start_date(self, date):
        self.url = self.url.replace(self.url_param.start_date, date)

    def set_end_date(self, date):
        self.url = self.url.replace(self.url_param.end_date, date)
