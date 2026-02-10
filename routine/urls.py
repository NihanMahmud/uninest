from django.urls import path
from . import views

urlpatterns = [
    # Fetch the logged-in student's routine
    path('', views.student_schedule, name='student_routine'),
]
