from model.url import URL
from model.urlparam import URLParam
from provider.google import Google
from datetime import datetime
import time
import copy


def obj_to_dict(obj):
    if isinstance(obj, datetime):
        return obj.__str__()
    return obj.__dict__


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

    routes = [
        ams_icn,
        ams_nrt
    ]

    g = Google()
    for route in routes:
        g.open_in_new_tab(route)
        time.sleep(2)
        for flight in g.parse():
            flight.insert()
    g.quit()
