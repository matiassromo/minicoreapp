from django.shortcuts import render
from .models import Gasto

def filtrar_gastos(request):
    gastos = []
    total_por_departamento = {}

    if request.method == 'GET' and 'fecha_inicio' in request.GET and 'fecha_fin' in request.GET:
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')
        
        # Filtrar los gastos por rango de fechas
        gastos = Gasto.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
        
        # Calcular el total por departamento
        for gasto in gastos:
            depto = gasto.empleado.departamento.nombre
            if depto not in total_por_departamento:
                total_por_departamento[depto] = 0
            total_por_departamento[depto] += gasto.monto

    return render(request, 'core/filtrar_gastos.html', {
        'gastos': gastos,
        'total_por_departamento': total_por_departamento,
    })
