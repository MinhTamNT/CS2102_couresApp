from django.contrib import admin
from .models import Category,Course,Lesson,Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class CategoryAmin(admin.ModelAdmin):
    list_display = ['id','name']
class CouresForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Course
        fields = '__all__'
class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['image']
    form = CouresForm
    def avatar(self, course):
        if course:
            return mark_safe(
            '<img src="/static/{url}" width="120" />'\
            .format(url=course.image.name)
        )

admin.site.register(Category,CategoryAmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Tag)

