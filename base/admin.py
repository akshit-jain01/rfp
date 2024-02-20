from django.contrib import admin

from .models import Vendor, Category, RequestForProposal, Quotes

# Register your models here.

admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(RequestForProposal)
admin.site.register(Quotes)