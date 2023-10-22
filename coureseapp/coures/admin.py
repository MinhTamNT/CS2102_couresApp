from django.contrib import admin
from .models import Category,Course
class CategoryAmin(admin.ModelAdmin):
    list_display = ['id','name']
# Register your models here.
admin.site.register(Category,CategoryAmin)
admin.site.register(Course)

