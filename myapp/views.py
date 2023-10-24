from cmath import log
from csv import reader
from email import message
import imp
from pyexpat.errors import messages
from turtle import title
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .models import crearCurso, Matricula, UserCourse, Programa
from .forms import crearCursoForms, crearMatricula
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

desarrollado = 'Estudiantes Ingenieria de Software - Universidad Cooperativa de Colombia '


def index(request):
    return render(request, 'dashboard/index.html', {
        'desarrollado': desarrollado
    })

@login_required
def signout(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'desarrollado': desarrollado
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'usuario o contraseña incorrectos',
                'desarrollado': desarrollado
            })
        else:
            login(request, user)
            return index(request)
        
def courses(request):
    cursos = crearCurso.objects.all()
    return render(request, 'courses/index.html', {
        'cursos': cursos,
    })

# def registerCourse(request):
#     return render(request, 'courses/forms/create.html')

# def editCourse(request):
#     return render(request, 'courses/forms/edit.html')

@login_required
def registerCourse(request):
    # print(idCurso)
    # us = request.user.username
    cursos = crearCurso.objects.all()
    programas =  Programa.objects.all()
    usuarios = UserCourse.objects.filter(rol="Profesor")
    profesor = UserCourse.objects.filter(identificacion="1085311455")
    print(profesor)
    # print(usuarios)
    if request.method == 'GET':
        
        return render(request, 'courses/forms/create.html', {
            'form': crearCursoForms(),
            'cursos': cursos,
            'usuarios': usuarios,
            'programas': programas
        })
    else:
        if profesor.exists():
            user_course = get_object_or_404(UserCourse, identificacion=profesor.first().identificacion)
        # profesor = UserCourse.objects.get(idCurso=idCurso)
            crearCurso.objects.create(idCurso=request.POST['idCourse'], 
                                    nombreCurso=request.POST['nombreCurso'], 
                                    numeroCreditos=request.POST['numeroCreditos'], 
                                    tipoPrograma=request.POST['tipoPrograma'], 
                                    programaPertenece=request.POST['programaPertenece'], 
                                    semestre=request.POST['semestre'],
                                    descripcion=request.POST['descripcion'],
                                    profesorCurso=user_course)
        return index(request)
    
def editCourse(request, id_Course):
    course = crearCurso.objects.get(idCurso=id_Course)
    
    if request.method == 'GET':
        data = {
            'course': course
        }
        return render(request, "courses/forms/editar_curso.html", data)
    else:
        course.idCurso=request.POST['idCourse']
        course.nombreCurso=request.POST['nombreCurso']
        course.numeroCreditos=request.POST['numeroCreditos']
        course.tipoPrograma=request.POST['tipoPrograma']
        course.programaPertenece=request.POST['programaPertenece']
        course.semestre=request.POST['semestre']
        course.descripcion=request.POST['descripcion']
        course.save()
        return redirect("/courses/")
    
@login_required
def matricularAlumno(request):
    alumnos = UserCourse.objects.filter(rol="Alumno")
    cursos = crearCurso.objects.all()
    if request.method == 'GET':
        
        return render(request, 'courses/forms/matricula.html', {
            'form': crearMatricula(),
            'alumnos': alumnos,
            'cursos': cursos
        })
    return index(request)
    
@login_required
def matriculaAlumnoGuardar(request, identificacion):
    print(identificacion)
    # cursos = crearCurso.objects.all()
    # print(us)
    # alumnos = UserCourse.objects.filter(rol="Alumno")
    # cursos = crearCurso.objects.all()
    alumnoMatricular = UserCourse.objects.filter(identificacion=identificacion)
    # cursoMAtricular = crearCurso.objects.filter(idCurso=curso)
    # print(alumnos)
    if request.method == 'POST':
        
    #     return render(request, 'courses/forms/matricula.html', {
    #         'form': crearMatricula(),
    #         'alumnos': alumnos,
    #         'cursos': cursos
    #     })
    # else:
        if alumnoMatricular.exists():
            alumnoMatriculado = get_object_or_404(UserCourse, identificacion=alumnoMatricular.first().identificacion)
            # cursoMatriculado = get_object_or_404(crearCurso, idCurso=cursoMAtricular.first().idCurso)
            Matricula.objects.create(alumno=alumnoMatriculado)
        return index(request)

@login_required
def gestNotas(request):
    return render(request, 'notes/index.html')

def profile(request):
    return render(request, 'profile/profile.html', {
        'desarrollado': desarrollado,
    })
