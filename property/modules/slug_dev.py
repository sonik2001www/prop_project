from load_django import *
from property.models import *


all_dev = Developer.objects.all()

for dev in all_dev:
    dev_name = dev.developer_name
    dev_slug = "-".join(str(dev_name).lower().split())
    try:
        dev.developer_slug = dev_slug
    except:
        index = 2
        while True:
            try:
                dev.developer_slug = dev_slug + f'-{index}'
                break
            except:
                index += 1
    dev.save()
