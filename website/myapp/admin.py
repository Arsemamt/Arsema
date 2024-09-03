from django.contrib import admin
from .models import Book, Category, Contact, Certificate

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','timestamp','message']
    list_filter = ['timestamp']
    search_fields = ('name',)

admin.site.register(Book)
admin.site.register(Category) 
admin.site.register(Certificate)
