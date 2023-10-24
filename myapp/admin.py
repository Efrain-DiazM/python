from django.contrib import admin
from .models import crearCurso, Programa, UserCourse, Matricula, Usuarios

admin.site.register(crearCurso)
admin.site.register(Programa)
admin.site.register(UserCourse)
admin.site.register(Matricula)
admin.site.register(Usuarios)