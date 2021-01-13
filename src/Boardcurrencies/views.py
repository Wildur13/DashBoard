from django.shortcuts import render, redirect

import api


def redirect_index(request):
    return redirect("press", days_r=7, currencies="USD")


# Create your views here.
def dashboard(request, days_r=70, currencies="CAD"):
    days, rates, n = api.get_rates(currencies=currencies.split(","), dayes=days_r)
    page_label = {7: "Week", 30: "Month", 365: "Year"}.get(days_r, "Customize")
    return render(request, "Boardcurrencies/index.html", context={"datas": rates,
                                                                  "days_labels": days,
                                                                  "currencies": currencies,
                                                                  "Dashboard": page_label,
                                                                  "number": n})
