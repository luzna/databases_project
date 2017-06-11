from django.contrib import admin
from .models import (
    Album,
    Author,
    Item,
    Order,
    Client
)


admin.site.register(Author)
admin.site.register(Album)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Client)
