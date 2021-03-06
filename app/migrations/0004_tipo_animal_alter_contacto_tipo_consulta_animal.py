# Generated by Django 4.0.2 on 2022-07-13 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreA', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.IntegerField(choices=[[0, 'consulta'], [0, 'reclamo'], [0, 'sugerencia'], [0, 'felicitaciones']]),
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreA', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('tipo_animal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_animal')),
            ],
        ),
    ]
