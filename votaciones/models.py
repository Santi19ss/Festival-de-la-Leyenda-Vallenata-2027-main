from django.db import models

class Edicion(models.Model):
    año = models.IntegerField(unique=True, verbose_name="Año de Edición")
    nombre_edicion = models.CharField(max_length=100, verbose_name="Nombre de la Edición")
    activa = models.BooleanField(default=True, verbose_name="¿Es la edición actual?")

    class Meta:
        verbose_name = "Edición"
        verbose_name_plural = "Ediciones"

    def __str__(self):
        return f"{self.año} - {self.nombre_edicion}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    estado = models.BooleanField(default=True, verbose_name="Activa")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

class Votacion(models.Model):
    edicion = models.ForeignKey(Edicion, on_delete=models.CASCADE, related_name='votaciones')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='votaciones_categoria')
    nombre_fase = models.CharField(max_length=150, verbose_name="Nombre de la Fase o Votación", help_text="Ej: Eliminatoria, Semifinal, Final")
    estado_apertura = models.BooleanField(default=False, verbose_name="¿Votación Abierta?")

    class Meta:
        verbose_name = "Votación"
        verbose_name_plural = "Votaciones"

    def __str__(self):
        return f"{self.categoria.nombre} - {self.nombre_fase} ({self.edicion.año})"

class Opcion(models.Model):
    votacion = models.ForeignKey(Votacion, on_delete=models.CASCADE, related_name='opciones')
    nombre_candidato = models.CharField(max_length=150, verbose_name="Nombre del Participante/Opción")
    biografia = models.TextField(blank=True, null=True, verbose_name="Biografía del Participante")

    class Meta:
        verbose_name = "Opción"
        verbose_name_plural = "Opciones"

    def __str__(self):
        return f"{self.nombre_candidato} ({self.votacion})"

class Voto(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='votos_festival')
    opcion = models.ForeignKey(Opcion, on_delete=models.PROTECT, related_name='votos')
    votacion = models.ForeignKey(Votacion, on_delete=models.CASCADE, related_name='votos')
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Voto'
        verbose_name_plural = 'Votos'
        constraints = [models.UniqueConstraint(fields=['usuario', 'votacion'], name='un_voto_por_usuario_y_votacion')]

    def __str__(self):
        return f'{self.usuario} - {self.votacion}'
