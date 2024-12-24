from django.urls import path
from .views import filtrar_gastos

urlpatterns = [
    path('', filtrar_gastos, name='filtrar_gastos'),
]
