from model.url import URL
from model.urlparam import URLParam
from model.googleflight import GoogleFlight
from provider.google import Google
from datetime import datetime
import time
import json


def obj_to_dict(obj):
    if isinstance(obj, datetime):
        return obj.__str__()
    return obj.__dict__


if __name__ == '__main__':
    gUrl = "https://www.google.com/flights#flt=[start_iata].[end_iata].[start_date]*" \
           "[end_iata].[start_iata].[end_date];c:EUR;e:1;sd:1;t:f"
    gUrl = URL(gUrl, URLParam(start_iata='[start_iata]', end_iata='[end_iata]',
                              start_date='[start_date]', end_date='[end_date]'))
    gUrl.set_route('AMS', 'ICN')
    gUrl.set_start_date('2020-04-09')
    gUrl.set_end_date('2020-04-23')

    g = Google()
    g.get(gUrl)
    time.sleep(2)  # windows closes before page can load completely
    flights: [GoogleFlight] = g.parse()
    print(json.dumps([x.__dict__ for x in flights], default=obj_to_dict))
    g.quit()
