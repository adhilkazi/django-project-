from django.contrib import admin
from .models import staff,cust



# class MemberAdmin(admin.ModelAdmin):

#   list_display = ("firstname","lastname","email","phonenumber","department","username","password")

# class MemberCustomer(admin.ModelAdmin):

#   list_display = ("firstname","lastname","email","phonenumber","state","username","password")

admin.site.register(staff)
admin.site.register(cust)

