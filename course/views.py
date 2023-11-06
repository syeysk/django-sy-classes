from django.views import View
from django.shortcuts import render, get_object_or_404

from course.models import Course, Module


class CoursesView(View):
    def get(self, request):
        courses = Course.objects.values('id', 'title')
        context = {'courses': courses}
        return render(request, 'course/course_list.html', context)


class ModulesView(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        modules = course.modules.values('id', 'title', 'description')
        context = {'modules': modules, 'course': course}
        return render(request, 'course/module_list.html', context)


class PartsView(View):
    def get(self, request, course_id, module_id):
        module = get_object_or_404(Module, pk=module_id, course__pk=course_id)
        parts = module.parts.all()

        parts_serialized = []
        for part in parts:
            lessons = []
            exercises = part.exercises.order_by('lesson_number').all()
            for exercise in exercises:
                lesson_number = exercise.lesson_number
                if len(lessons) != lesson_number:
                    lessons.append([])

                lessons[lesson_number - 1].append(exercise)

            parts_serialized.append(
                {
                    'id': part.id,
                    'title': part.title,
                    'description': part.description,
                    'lessons': lessons,
                }
            )
        context = {'parts': parts_serialized, 'module': module}
        return render(request, 'course/part_list.html', context)


class ExerciseView(View):
    def get(self, request, part_id, lesson_number):
        context = {}
        return render(request, 'course/exercise.html', context)
