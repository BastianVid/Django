from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, vervose_name='Id de la Categoria')
    NombreCategoria = models.CharField(max_length=50, vervose_name= 'Nombre de la Categoria')

    def __str__(self):
        return self.NombreCategoria