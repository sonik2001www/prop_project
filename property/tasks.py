import os

from .modules.hipflat_3v1 import parsing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prop_project.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


async def start_parsing(username, url, bind=True):
    parsing(username, url)
