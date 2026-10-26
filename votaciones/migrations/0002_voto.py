from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [('votaciones', '0001_initial'), migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [migrations.CreateModel(name='Voto', fields=[
        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('fecha', models.DateTimeField(auto_now_add=True)),
        ('opcion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='votos', to='votaciones.opcion')),
        ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votos_festival', to=settings.AUTH_USER_MODEL)),
        ('votacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votos', to='votaciones.votacion')),
    ],options={'verbose_name':'Voto','verbose_name_plural':'Votos'}),
    migrations.AddConstraint(model_name='voto',constraint=models.UniqueConstraint(fields=('usuario','votacion'),name='un_voto_por_usuario_y_votacion'))]
