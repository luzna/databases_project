import os
from store_app.models import *


os.environ['DJANGO_SETTINGS_MODULE'] = 'store.settings'
author1 = Author(name='Joe', surname='Bonamassa')
author1.save()
