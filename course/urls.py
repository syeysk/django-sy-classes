from django.urls import path

from course.views import CoursesView, ExerciseView, ModulesView, PartsView

urlpatterns = [
    path('', CoursesView.as_view(), name='course_list'),
    path('<int:course_id>/', ModulesView.as_view(), name='module_list'),
    path('<int:course_id>/module/<int:module_id>', PartsView.as_view(), name='part_list'),
    path('part/<int:part_id>/lesson/<int:lesson_number>', ExerciseView.as_view(), name='exercise'),
]
