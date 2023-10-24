from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('logout/', views.signout, name="logout"),
    path('', views.signin, name="signin"),
    path('courses/', views.courses, name="courses"),
    path('index/', views.index, name="dashboard"),
    path('registerCourse/', views.registerCourse, name="registerCourse"),
    # path('registerCourse/<int:idCurso>', views.registerCourse, name="registerCourse"),
    path('editCourse/<int:id_Course>', views.editCourse, name="edit_Course"),
    path('matricula/', views.matricularAlumno, name="matricula"),
    path('/matriculaRealizada/<int:identificacion>/<int:idCurso>', views.matriculaAlumnoGuardar, name="matriculaAlumnoGuardar"),
    path('notas/', views.gestNotas, name="notas"),
    # path('crearCursos/', views.crearCursos, name="crearCursos"),
    path('profile/', views.profile, name="profile"),
]