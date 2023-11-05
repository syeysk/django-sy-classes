from django.views import View
from django.shortcuts import render, get_object_or_404

from course.models import Course


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
