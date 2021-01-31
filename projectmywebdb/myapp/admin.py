from django.contrib import admin

# Register your models here.
from myapp.models import Product
from myapp.models import Manufactory

admin.site.register(Product)
admin.site.register(Manufactory)
