from django.urls import path

from AppCoder.views.profesores import leerProfesores, profesorFormulario, eliminarProfesor, editarProfesor
from AppCoder.views.other import cursos , profesores, estudiantes, entregables, inicio, busquedaCamada, buscar
from AppCoder.views.cursos import CursoListView, CursoDetailView, CursoCreateView, CursoUpdateView, CursoDeleteView

urlpatterns = [
    # path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    # path('estudiantes/<int:pk>/', detalle_estudiante, name='detalle_estudiante'),
    path('', inicio, name='inicio'),
    # path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),

    # path('busquedaCamada', busquedaCamada, name="busquedaCamada"),
    path('buscar/', buscar, name='buscar'),

    path('profesores/', leerProfesores, name='profesores'),
    path('profesorFormulario/', profesorFormulario, name="profesorFormulario"),
    path('eliminarProfesor/<int:id_profesor>', eliminarProfesor, name="eliminarProfesor"),
    path('editarProfesor/<int:id_profesor>', editarProfesor, name="editarProfesor"),


    path('cursos/', CursoListView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoDetailView.as_view(), name='cursos_detail'),
    path('cursos/nuevo/', CursoCreateView.as_view(), name='cursos_new'),
    path('cursos/editar/<int:pk>/', CursoUpdateView.as_view(), name='cursos_edit'),
    path('cursos/borrar/<int:pk>/', CursoDeleteView.as_view(), name='cursos_delete'),
]
