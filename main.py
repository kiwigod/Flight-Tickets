from selenium import webdriver
from model.url import URL
from model.urlparam import URLParam
from provider.google import Google
import copy


if __name__ == '__main__':
    gBaseUrl = "https://www.google.com/flights#flt=[start_iata].[end_iata].[start_date]*" \
               "[end_iata].[start_iata].[end_date];c:EUR;e:1;sd:1;t:f"
    gParamUrl = URL(gBaseUrl, URLParam(start_iata='[start_iata]', end_iata='[end_iata]',
                                       start_date='[start_date]', end_date='[end_date]'))
    gParamUrl.set_start_date('2020-04-09')
    gParamUrl.set_end_date('2020-04-23')

    ams_icn = copy.deepcopy(gParamUrl)
    ams_icn.set_route('AMS', 'ICN')

    ams_nrt = copy.deepcopy(gParamUrl)
    ams_nrt.set_route('AMS', 'NRT')

    ams_sin = copy.deepcopy(gParamUrl)
    ams_sin.set_route('AMS', 'SIN')

    routes = [
        ams_icn,
        ams_nrt,
        ams_sin
    ]

    g = Google(webdriver.Firefox())
    for route in routes:
        g.open_in_new_tab(route)
        flights = g.parse()
        if flights is None:
            continue
        for flight in flights:
            flight.insert()
    g.quit()
