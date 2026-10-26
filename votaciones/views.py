from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Edicion, Categoria, Votacion, Opcion, Voto

def index(request):
    ediciones = Edicion.objects.all().order_by('-año')
    return render(request, 'votaciones/index.html', {'ediciones': ediciones})

def lista_categorias(request):
    categorias = Categoria.objects.filter(estado=True, votaciones_categoria__edicion__activa=True).distinct().order_by('nombre')
    return render(request, 'votaciones/categorias.html', {'categorias': categorias})

def detalle_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id, estado=True)
    votaciones = (Votacion.objects.filter(categoria=categoria, edicion__activa=True)
                  .select_related('edicion').prefetch_related('opciones').order_by('-edicion__año','nombre_fase'))
    votos_realizados = set()
    if request.user.is_authenticated:
        votos_realizados = set(Voto.objects.filter(usuario=request.user, votacion__in=votaciones)
                               .values_list('votacion_id', flat=True))
    return render(request, 'votaciones/detalle_categoria.html', {
        'categoria': categoria, 'votaciones': votaciones, 'votos_realizados': votos_realizados,
    })

@login_required(login_url='login')
@require_POST
def registrar_voto(request, votacion_id):
    votacion = get_object_or_404(Votacion, pk=votacion_id, categoria__estado=True,
                                edicion__activa=True, estado_apertura=True)
    opcion = get_object_or_404(Opcion, pk=request.POST.get('opcion'), votacion=votacion)
    try:
        with transaction.atomic():
            Voto.objects.create(usuario=request.user, votacion=votacion, opcion=opcion)
    except IntegrityError:
        messages.warning(request, 'Ya registraste tu voto en esta votación.')
    else:
        messages.success(request, '¡Tu voto se registró correctamente!')
    return redirect('votaciones:detalle_categoria', categoria_id=votacion.categoria_id)

def contacto(request):
    return render(request, 'votaciones/contacto.html')


def detalle_edicion(request, año):
    edicion = get_object_or_404(Edicion, año=año)
    votaciones = (Votacion.objects.filter(edicion=edicion)
                  .select_related('categoria').prefetch_related('opciones')
                  .order_by('categoria__nombre', 'nombre_fase'))
    grupos = {}
    for votacion in votaciones:
        grupo = grupos.setdefault(votacion.categoria_id, {'categoria': votacion.categoria, 'votaciones': []})
        grupo['votaciones'].append(votacion)
    return render(request, 'votaciones/detalle_edicion.html', {
        'edicion': edicion, 'grupos': list(grupos.values()),
    })
