from django.contrib import admin
from .models import StripeCustomer, MyTutorCustomer

admin.site.register(StripeCustomer)
admin.site.register(MyTutorCustomer)
