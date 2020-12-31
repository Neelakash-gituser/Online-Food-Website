from django.contrib import admin

# Register your models here.
from . models import Food , Contact ,Buy

admin.site.register(Food)
admin.site.register(Contact)
admin.site.register(Buy)
