from django.contrib import admin
from . models import employees
from . models import client

admin.site.register(employees)
admin.site.register(client)

# Register your models here.
