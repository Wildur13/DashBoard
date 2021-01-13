import datetime
from pprint import pprint

import requests
import os
import json


def get_rates(currencies, dayes=30):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=dayes)

    join = ','.join(currencies)
    requete = f"https://api.exchangeratesapi.io/history?start_at={start_date}&end_at={end_date}&symbols={join}"
    r = requests.get(requete)
    if not r and not r.json():
        return False, False
    api_rates = r.json().get("rates")
    all_rates = {currency: [] for currency in currencies}
    all_days = sorted(api_rates.keys())
    for eachD in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[eachD].items()]

    return all_days, all_rates, dayes


def get_data(c="Kaiserslautern"):
    d = {"Kaiserslautern": {
        "2020-10-04": {"Java": 5,
                       "Python": 3,
                       "Xamarin": 2
                       },
        "2020-10-03": {"Java": 8,
                       "Python": 2,
                       "Xamarin": 9
                       }
    },
        "Karlsruhe": {
            "2020-10-04": {"Java": 4,
                           "Python": 8,
                           "Xamarin": 2,
                           "JavaScript": 15,
                           "Angular": 7,
                           "Node.js": 3
                           },
            "2020-09-03": {"Java": 8,
                           "Python": 10,
                           "Xamarin": 1,
                           "JavaScript": 10,
                           "Angular": 5,
                           "Node.js": 6
                           },
            "2020-08-02": {"Java": 5,
                           "Python": 9,
                           "Xamarin": 14,
                           "JavaScript": 18,
                           "Angular": 2,
                           "Node.js": 9
                           },
            "2020-07-01": {"Java": 7,
                           "Python": 20,
                           "Xamarin": 10,
                           "JavaScript": 8,
                           "Angular": 7,
                           "Node.js": 3
                           }
        }
    }
    chemin = os.path.dirname(__file__)
    data = os.path.join(chemin, "data.json")
    with open(data, 'r') as f:
        l = json.load(f)
    r = d.get(c)
    all_rates = {currency: [] for currency in l}
    all_days = sorted(r.keys())
    #k = [key for key, r in all_rates.items()]
    #p = [val for key, val in all_rates.items()]
    for eachD in all_days:
         [all_rates[skill].append(rate) for skill, rate in r[eachD].items()]
    return all_days, all_rates, c


if __name__ == '__main__':
    days, rates, get = get_rates(currencies=["USD", "CAD"])
    day, items, s = get_data(c="Karlsruhe")
    print(items)
