from load_django import *
from property.models import *


all_over = Overview.objects.all()

for over in all_over:
    over_name = over.name_overview
    over_slug = "-".join(str(over_name).lower().split())
    try:
        over.overview_slug = over_slug
        over.save()
    except:
        index = 2
        while True:
            try:
                over.overview_slug = over_slug + f'-{index}'
                over.save()
                break
            except:
                index += 1

