from django.db import models
from decimal import Decimal

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=255, verbose_name="Joylashuv")
    
    def __str__(self) -> str:
        return self.location
        
    class Meta:
        verbose_name = 'Joylashuv'
        verbose_name_plural = verbose_name + 'lar'
        
        
class Buildings(models.Model):
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Nomi")
    
    def __str__(self) -> str:
        return f"{self.location}, {self.name}"
    
    class Meta:
        verbose_name = 'Bino'
        verbose_name_plural = verbose_name + 'lar'
    
class Floor(models.Model):
    building = models.ForeignKey(to=Buildings, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name="Qavat raqami")
    
    def __str__(self) -> str:
        return f"{self.building}, {self.number} - qavat"

    class Meta:
        verbose_name = 'Qavat'
        verbose_name_plural = verbose_name + 'lar'
    
class Home(models.Model):
    building = models.ForeignKey(to=Floor, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name="Uy raqami")
    room = models.IntegerField(verbose_name="Uydagi xonalar soni")
    square = models.BigIntegerField(verbose_name="m² maydon narxi")
    total_area = models.BigIntegerField(verbose_name="Umumiy maydoni")
    
    def __str__(self) -> str:
        return f"{self.building}, {self.number} - Uy, {self.room} xonali"

    class Meta:
        verbose_name = 'Uy'
        verbose_name_plural = verbose_name + 'lar'
    

from django.db import models
from decimal import Decimal

class Clients(models.Model):
    terms = [
        ('---', '---'),
        (5, '5 yil'),
        (6, '6 yil'),
        (7, '7 yil'),
        (8, '8 yil'),
        (9, '9 yil'),
        (10, '10 yil'),
        (11, '11 yil'),
        (12, '13 yil'),
        (14, '14 yil'),
        (15, '15 yil'),
        (16, '16 yil'),
        (17, '17 yil'),
        (18, '18 yil'),
        (19, '19 yil'),
        (20, '20 yil')
    ]
    
    STATUS_CHOICES = (
        ('0', 'O\'ylab Ko\'rmoqchi'),
        ('1', 'Sotib Olmoqchi'),
        ('2', 'Sotib oldi'),
    )
    
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE, verbose_name="Joylashuv")
    building = models.ForeignKey(to=Buildings, on_delete=models.CASCADE, verbose_name="Bino")
    floor = models.ForeignKey(to=Floor, on_delete=models.CASCADE, verbose_name="Qavat")
    home = models.ForeignKey(to=Home, on_delete=models.CASCADE, verbose_name="Uy")
    fish = models.CharField(max_length=255, verbose_name="F.I.SH")
    telefon = models.IntegerField(verbose_name="Telfon")
    term = models.IntegerField(choices=terms, default="---", verbose_name="To'lov muddati")
    oylik_tolov = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='0')

    @property
    def narx(self):
        if self.home:
            return Decimal(self.home.square) * Decimal(self.home.total_area)
        return Decimal(0)

    def save(self, *args, **kwargs):
        if self.home and self.term != '---':
            yillik_tolovlar_soni = int(self.term) * 12
            self.oylik_tolov = self.narx / Decimal(yillik_tolovlar_soni)
        else:
            self.oylik_tolov = Decimal(0)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.fish

    class Meta:
        verbose_name = 'Mijoz'
        verbose_name_plural = verbose_name + 'lar'

    
class News(models.Model):
    
    text = models.TextField(verbose_name="Xabar matni")
    
    def __str__(self) -> str:
        return f"{str(self.text[:20])}..."
    
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = verbose_name + 'lar'
        
    