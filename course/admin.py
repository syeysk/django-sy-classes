from django.contrib import admin

from course.models import Course, Exercise, Module, Part, Relation


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'description')


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'module', 'title', 'description')


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'answer', 'theme', 'source')


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'part', 'lesson_number', 'relation')
