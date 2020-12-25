from django.db import models

# Create your models here.

class County(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class RainData(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    # County = models.CharField(max_length=5)
    siteId = models.CharField('測站代碼', max_length=5)
    siteName = models.CharField('測站名稱', max_length=5)
    itemId = models.CharField('測項代碼', max_length=5)
    itemName = models.CharField('測項名稱', max_length=10)
    itemEngName = models.CharField('測項英文名稱', max_length=20)
    itemUnit = models.CharField('測項單位', max_length=10)
    monitorDate = models.CharField('監測日期', max_length=20)
    time = models.DateTimeField(auto_now=True)
    concentration = models.FloatField('數值')

    def __str__(self):
        return self.siteName
