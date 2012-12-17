from django.db import models

# Create your models here.


class Foto(models.Model):
  titulo = models.CharField(max_length=256)
  arquivo = models.FileField(upload_to="fotos")

  def __unicode__(self):
    return "%s" % self.titulo


class Carro(models.Model):
  fabricante = models.CharField(max_length=256) 
  modelo = models.CharField(max_length=256)
  preco = models.DecimalField(decimal_places=2,max_digits=9)
  wiki = models.CharField(max_length=1024)
  album = models.FileField(upload_to="fotos/")
  notaMecanica = models.IntegerField()
  notaMediaGeral = models.IntegerField()
  notaTorque = models.IntegerField()
  notaLataria = models.IntegerField()
  notaInterior= models.IntegerField()
  notaAcessorios = models.IntegerField()
  
  
  def __unicode__(self):
    return "%s" % self.modelo