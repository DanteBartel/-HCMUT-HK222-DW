from django.db import models

# Create your models here.
class Sector(models.Model):
    name = models.CharField(max_length=100, null=False)

class Ticker(models.Model):
    ticker = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)

class PriceDim(models.Model):
    date = models.DateField()
    price = models.FloatField(null=False)

class Stock(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.SET_NULL, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
    stock_growth = models.FloatField(null=True)