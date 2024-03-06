import sys
import os
import django

sys.path.append('/Users/applebuy/PycharmProjects/property/prop_project')  # Change Path
os.environ['DJANGO_SETTINGS_MODULE'] = 'prop_project.prop_project.settings'  # Project name
django.setup()
