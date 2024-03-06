from load_django import *
from property.models import *


all_proj = Property.objects.all()

for proj in all_proj:
    proj_name = proj.condo_name
    proj_slug = "-".join(str(proj_name).lower().split())
    try:
        proj.property_slug = proj_slug
        proj.save()
    except:
        index = 2
        while True:
            try:
                proj.property_slug = proj_slug + f'-{index}'
                proj.save()
                break
            except:
                index += 1
