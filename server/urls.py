from django.contrib import admin
from django.urls import path, include

from django_sy_framework.base.views import (
    MicroservicesListView,
    ProfileView,
    RobotsTxtView,
)

from course.views import CoursesView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('server.urls_api')),
    path('auth/', include('django_sy_framework.custom_auth.urls')),
    path('course/', include('course.urls')),
    # path('', include('django_sy_framework.base.urls')),

    path('', CoursesView.as_view(), name='index'),
    path('all-microservices/', MicroservicesListView.as_view(), name='microservices'),
    path('profile/', ProfileView.as_view(), name='custom_profile'),
]
