# Generated by Django 3.2.13 on 2023-09-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('nota_geral', models.IntegerField()),
                ('problemas', models.CharField(max_length=70)),
                ('frequencia', models.CharField(choices=[('Q', 'Quase nunca vou'), ('F', 'Frequentemente'), ('S', 'Sempre')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='NaoKennedy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('nivel_ruim', models.IntegerField()),
                ('regularidade', models.CharField(choices=[('S', 'Sempre'), ('O', 'Ocasionalmente'), ('N', 'Nunca')], max_length=1)),
                ('insatisfacao', models.CharField(choices=[('G', 'Grande'), ('C', 'Controlável'), ('D', 'Drama pessoal')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tabela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('nota', models.FloatField()),
            ],
        ),
    ]
