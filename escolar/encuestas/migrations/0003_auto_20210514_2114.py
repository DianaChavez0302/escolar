# Generated by Django 3.2 on 2021-05-15 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('encuestas', '0002_alter_pregunta_texto_pregunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='creador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='fecha_pub',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha de publicacion'),
        ),
    ]
