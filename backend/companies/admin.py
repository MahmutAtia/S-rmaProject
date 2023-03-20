from django.contrib import admin
from .models import (Company,Contact,ContactResult,ContactType)

# Register your models here.
admin.site.register([Company,Contact,ContactResult,ContactType])
