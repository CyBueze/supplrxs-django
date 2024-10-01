from django.contrib import admin
from .models import Supplier, State, Drug

admin.site.register(Supplier)
admin.site.register(State)
admin.site.register(Drug)