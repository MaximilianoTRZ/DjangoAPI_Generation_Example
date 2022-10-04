from django.contrib import admin

from .models.addressModel import Address
from .models.clientModel import Client
from .models.cityModel import City


admin.site.register(City)
admin.site.register(Client)
admin.site.register(Address)