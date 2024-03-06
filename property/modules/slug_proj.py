from load_django import *
from property.models import *


all_pro = Project.objects.all()

for pro in all_pro:
    pro_name = pro.project_name
    pro_slug = "-".join(str(pro_name).lower().split())
    try:
        pro.project_slug = pro_slug
        pro.save()
    except:
        index = 2
        while True:
            try:
                pro.project_slug = pro_slug + f'-{index}'
                pro.save()
                break
            except:
                index += 1
