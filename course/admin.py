from django.contrib import admin

from course.models import Course, Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'description')
