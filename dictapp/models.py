from django.db import models

#from django.conf import settings


class dictclass(models.Model):
    id =            models.AutoField(primary_key=True)
    Ordem = models.CharField(max_length=3, blank=True, default='')
    palavra =       models.CharField(max_length=255, blank=True, default='')
    palavratrad =   models.CharField(max_length=1000, blank=True, default='')
    frase =         models.CharField(max_length=1000, blank=True, default='')
    frasetrad =     models.CharField(max_length=1000, blank=True, default='')
    frase2 =        models.CharField(max_length=1000, blank=True, default='')
    frasetrad2 =    models.CharField(max_length=1000, blank=True, default='')
    frase3 =        models.CharField(max_length=1000, blank=True, default='')
    frasetrad3 =    models.CharField(max_length=1000, blank=True, default='')
    figura1 =       models.CharField(max_length=1000, null=False, blank=False)
    som1 =          models.CharField(max_length=1000, null=False, blank=False)
    suaresposta1 =   models.TextField(max_length=1000, blank=True, default='')
    suaresposta2 =   models.TextField(max_length=1000, blank=True, default='')
    suaresposta3 =   models.TextField(max_length=1000, blank=True, default='')

    def __str__(self):
        return self.palavra + ' ' + self.frase

    objects = models.Manager()
    objetos = models.Manager()

