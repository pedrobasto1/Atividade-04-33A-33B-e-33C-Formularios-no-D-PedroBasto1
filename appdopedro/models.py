from django.db import models

class Lugares(models.Model):
  OPTIONS = [
    ("Q", "Quase nunca vou"),
    ("F", "Frequentemente"),
    ("S", "Sempre")
  ]
  titulo = models.CharField(max_length=50)
  nota_geral = models.IntegerField()
  problemas = models.CharField(max_length=70)
  frequencia = models.CharField(max_length=1, choices=OPTIONS)

class NaoKennedy(models.Model):
  INSATISFACAO = [
    ("G", "Grande"),
    ("C", "Controlável"),
    ("D", "Drama pessoal")
  ]
  REGULARIDADE = [
    ("S", "Sempre"),
    ("O", "Ocasionalmente"),
    ("N", "Nunca")
  ]
  titulo = models.CharField(max_length=50)
  nivel_ruim = models.IntegerField()
  regularidade = models.CharField(max_length=1, choices=REGULARIDADE)
  insatisfacao = models.CharField(max_length=1, choices=INSATISFACAO)

class Tabela(models.Model):
  titulo= models.CharField(max_length=50)
  nota=models.FloatField()
 