from django.contrib import admin
from userauth import models
# Register your models here.
admin.site.register(models.Account)
admin.site.register(models.Address)

