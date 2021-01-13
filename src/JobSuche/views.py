from django.shortcuts import render


import api


# Create your views here.


def jobSuche(request, stadt="Kaiserslautern"):
    days, items, city = api.get_data(c=stadt)
    return render(request, "JobSuche/page.html", context={"stadt": city,
                                                          "dates": days,
                                                          "items": items
                                                          })


