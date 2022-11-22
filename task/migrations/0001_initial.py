# Generated by Django 4.1.3 on 2022-11-20 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Turista',
            fields=[
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('edad', models.IntegerField()),
                ('pais', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=255)),
                ('forma_pago', models.CharField(choices=[('D', 'Debito'), ('C', 'Credito'), ('E', 'Efectivo')], max_length=1)),
                ('correo', models.CharField(max_length=255)),
                ('telefono', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Turista',
                'verbose_name_plural': 'Turista',
            },
        ),
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acompanante', models.BooleanField()),
                ('fecha_llegada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('T_transporte', models.CharField(max_length=255)),
                ('Aprox_gasto', models.IntegerField()),
                ('equipo', models.TextField()),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cuestionado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.turista')),
            ],
            options={
                'verbose_name': 'Cuestionario',
                'verbose_name_plural': 'Cuestionarios',
            },
        ),
    ]
