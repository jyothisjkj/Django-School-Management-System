from django.urls import path
from . import views


urlpatterns = [
    path("",views.student_login,name="student-login")

]
