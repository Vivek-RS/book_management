from django.contrib import admin

from bookdetails.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Author)
admin.site.register(Book)