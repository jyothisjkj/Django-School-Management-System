from django.urls import path 
from . import views

urlpatterns = [
    path("",views.staff_login, name="staff-login"),
    path("signup/",views.staff_signup,name="staff-signup"),
    path("home-page/",views.staff_loginpage, name="staff-loginpage"),
    path("logout/",views.logout_section,name="logout-section"),
    path("add_student/",views.add_student,name="add-student"),
    path("delete_student/<roll_number>",views.delete_student,name="delete-student"),
    path("update_student/<roll_number>",views.update_student,name="update-student"),
]
