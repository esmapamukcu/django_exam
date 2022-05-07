from django.db import models



# Create your models here.
class Ogrenci(models.Model):
    ad=models.CharField(max_length=50)
    soyad=models.CharField(max_length=50)
    bolum=models.CharField(max_length=50)
    tckn=models.CharField(max_length=50, primary_key=True)
    vize = models.FloatField(max_length=50)
    final = models.FloatField(max_length=50)
    ortalama = models.FloatField(max_length=50)
    harfnotu = models.CharField(max_length=50)

    def __str__(self):
        return "%s"%(self.ad)
