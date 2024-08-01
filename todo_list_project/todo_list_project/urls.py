# todo_list_project/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import index  # Importar a view index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
    path('', index),  # Adicionar a rota para a página inicial
]
