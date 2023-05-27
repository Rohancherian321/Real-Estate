from django.contrib import admin
from.models import *

admin.site.register(Buyerreg)
admin.site.register(Property)
admin.site.register(Book)


class Owneradmin(admin.ModelAdmin):
    list_display=('oid','oname')
    search_fields = ('oid','oname')

admin.site.register(Ownerreg,Owneradmin)

# Register your models here.
