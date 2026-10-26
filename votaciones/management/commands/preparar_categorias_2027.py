from django.core.management.base import BaseCommand
from votaciones.models import Edicion, Categoria, Votacion, Opcion

CATEGORIAS = [
    ("Acordeón Profesional – Rey de Reyes", "Competencia especial de acordeonistas en la edición Rey de Reyes de 2027."),
    ("Reina de Reinas", "Modalidad especial de acordeonistas mujeres anunciada para 2027."),
    ("Piquería Mayor – Rey de Reyes", "Concurso de improvisación y versos en la edición Rey de Reyes."),
    ("Canción Vallenata Inédita – Rey de Reyes", "Modalidad dedicada a composiciones vallenatas inéditas."),
]

class Command(BaseCommand):
    help = 'Prepara categorías anunciadas para 2027; opcionalmente crea votaciones y opciones de prueba cerradas.'

    def add_arguments(self, parser):
        parser.add_argument('--demo', action='store_true', help='Crea opciones ficticias etiquetadas de prueba (no oficiales).')

    def handle(self, *args, **options):
        edicion, _ = Edicion.objects.get_or_create(año=2027, defaults={'nombre_edicion': '60.º Festival – Rey de Reyes', 'activa': True})
        for nombre, descripcion in CATEGORIAS:
            categoria, created = Categoria.objects.get_or_create(nombre=nombre, defaults={'descripcion': descripcion, 'estado': True})
            if not created and not categoria.descripcion:
                categoria.descripcion = descripcion
                categoria.save(update_fields=['descripcion'])
            if options['demo']:
                votacion, _ = Votacion.objects.get_or_create(edicion=edicion, categoria=categoria, nombre_fase='Demostración académica (NO OFICIAL)', defaults={'estado_apertura': False})
                for n in range(1, 4):
                    Opcion.objects.get_or_create(votacion=votacion, nombre_candidato=f'Opción de prueba {n}', defaults={'biografia': 'Dato ficticio para probar el sistema. No representa a una persona inscrita en 2027.'})
        self.stdout.write(self.style.SUCCESS('Categorías 2027 preparadas. ' + ('Demostraciones cerradas agregadas.' if options['demo'] else 'Sin participantes inventados.')))
