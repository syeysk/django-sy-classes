from django.urls import path

from course.views import CoursesView, ModulesView

urlpatterns = [
    path('', CoursesView.as_view(), name='course_list'),
    path('<int:course_id>/', ModulesView.as_view(), name='module_list'),
]
